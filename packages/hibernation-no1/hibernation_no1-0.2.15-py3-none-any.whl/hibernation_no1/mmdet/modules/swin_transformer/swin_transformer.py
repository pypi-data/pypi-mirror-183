
import torch
import torch.nn as nn
import torch.nn.functional as F

from hibernation_no1.utils.log import LOGGERS

from hibernation_no1.mmdet.utils import to_2tuple
from hibernation_no1.mmdet.checkpoint import load_checkpoint
from hibernation_no1.mmdet.modules.base.module import BaseModule, ModuleList
from hibernation_no1.mmdet.modules.base.initialization.constant import constant_init
from hibernation_no1.mmdet.modules.base.initialization.normal import trunc_normal_init

from hibernation_no1.mmdet.modules.swin_transformer.patch import PatchEmbed, PatchMerging
from hibernation_no1.mmdet.modules.swin_transformer.swin_block import SwinBlockSequence



class SwinTransformer(BaseModule):
    """ Swin Transformer
    A PyTorch implement of : `Swin Transformer:
    Hierarchical Vision Transformer using Shifted Windows`  -
        https://arxiv.org/abs/2103.14030

    Inspiration from
    https://github.com/microsoft/Swin-Transformer

    Args:
        pretrain_img_size (int | tuple[int]): The size of input image when
            pretrain. Defaults: 224.
        in_channels (int): The num of input channels.
            Defaults: 3.
        embed_dims (int): The feature dimension. Default: 96.
        patch_size (int | tuple[int]): Patch size. Default: 4.
        window_size (int): Window size. Default: 7.
        mlp_ratio (int): Ratio of mlp hidden dim to embedding dim.
            Default: 4.
        depths (tuple[int]): Depths of each Swin Transformer stage.
            Default: (2, 2, 6, 2).
        num_heads (tuple[int]): Parallel attention heads of each Swin
            Transformer stage. Default: (3, 6, 12, 24).
        strides (tuple[int]): The patch merging or patch embedding stride of
            each Swin Transformer stage. (In swin, we set kernel size equal to
            stride.) Default: (4, 2, 2, 2).
        out_indices (tuple[int]): Output from which stages.
            Default: (0, 1, 2, 3).
        qkv_bias (bool, optional): If True, add a learnable bias to query, key,
            value. Default: True
        qk_scale (float | None, optional): Override default qk scale of
            head_dim ** -0.5 if set. Default: None.
        drop_rate (float): Dropout rate. Defaults: 0.
        attn_drop_rate (float): Attention dropout rate. Default: 0.
        drop_path_rate (float): Stochastic depth rate. Defaults: 0.1.
        use_abs_pos_embed (bool): If True, add absolute position embedding to
            the patch embedding. Defaults: False.
        norm_cfg (dict): Config dict for normalization layer at
            output of backone. Defaults: dict(type='LN').
        with_cp (bool, optional): Use checkpoint or not. Using checkpoint
            will save some memory while slowing down the training speed.
            Default: False.
        pretrained (str, optional): model pretrained path. Default: None.
        convert_weights (bool): The flag indicates whether the
            pre-trained model is from the original repo. We may need
            to convert some keys to make it compatible.
            Default: False.
        frozen_stages (int): Stages to be frozen (stop grad and set eval mode).
            Default: -1 (-1 means not freezing any parameters).
        init_cfg (dict, optional): The Config for initialization.
            Defaults to None.
    """
    # delete `absolute position embedding``
    def __init__(self,
                 pretrain_img_size=224,
                 in_channels=3,
                 embed_dims=96,
                 patch_size=4,
                 window_size=7,
                 mlp_ratio=4,
                 depths=(2, 2, 6, 2),
                 num_heads=(3, 6, 12, 24),
                 strides=(4, 2, 2, 2),
                 out_indices=(0, 1, 2, 3),
                 qkv_bias=True,
                 qk_scale=None,
                 pm_kernel_size = 2,
                 pm_dilation = 1,
                 drop_rate=0.,
                 attn_drop_rate=0.,
                 drop_path_rate=0.1,
                 with_cp=False,
                 convert_weights=False,
                 frozen_stages=-1,
                 init_cfg=None):    
        
        self.convert_weights = convert_weights  
        self.frozen_stages = frozen_stages   
        if isinstance(pretrain_img_size, int):
            pretrain_img_size = to_2tuple(pretrain_img_size)        # (224, 224)  
        elif isinstance(pretrain_img_size, tuple):
            if len(pretrain_img_size) == 1:
                pretrain_img_size = to_2tuple(pretrain_img_size[0])
            assert len(pretrain_img_size) == 2, \
                f'The size of image should have length 1 or 2, ' \
                f'but got {len(pretrain_img_size)}'
                
        super(SwinTransformer, self).__init__(init_cfg=init_cfg)
    
        num_layers = len(depths)
        self.out_indices = out_indices

        assert strides[0] == patch_size,  'Use non-overlapping patch embed.'
        
        self.patch_embed = PatchEmbed(
            in_channels=in_channels,
            embed_dims=embed_dims,
            kernel_size=patch_size,
            stride=strides[0],
            init_cfg=None)
        
        self.drop_after_pos = nn.Dropout(p=drop_rate) 
        
        # set stochastic depth decay rule
        total_depth = sum(depths)
        dpr = [
            x.item() for x in torch.linspace(0, drop_path_rate, total_depth)
        ]     
        
        self.stages = ModuleList()
                
        in_channels = embed_dims
        for i in range(num_layers):
            if i < num_layers - 1:
                downsample = PatchMerging(
                    in_channels=in_channels,
                    out_channels=2 * in_channels,
                    kernel_size = pm_kernel_size,
                    dilation = pm_dilation,
                    stride=strides[i + 1],
                    init_cfg=None)
            else:
                downsample = None  # don't apply `downsample` at last layer
                
            
            stage = SwinBlockSequence(
                embed_dims=in_channels,
                num_heads=num_heads[i],
                feedforward_channels=mlp_ratio * in_channels,
                depth=depths[i],
                window_size=window_size,
                qkv_bias=qkv_bias,
                qk_scale=qk_scale,
                drop_rate=drop_rate,
                attn_drop_rate=attn_drop_rate,
                drop_path_rate=dpr[sum(depths[:i]):sum(depths[:i + 1])],
                downsample=downsample,
                with_cp=with_cp,
                init_cfg=None)  
            self.stages.append(stage)                 
            
            if downsample:  in_channels = downsample.out_channels
        self.num_features = [int(embed_dims * 2**i) for i in range(num_layers)]
        
        for i in out_indices:
            layer = nn.LayerNorm(self.num_features[i], eps= 1e-05)
            for param in layer.parameters():
                param.requires_grad = True
            layer_name = f'norm{i}'
            self.add_module(layer_name, layer)
        
    # B: batch_size, C: Channel, H: height, W: width
    def forward(self, x):       # [B_init, C_init, H_init, W_init]
        
        x, hw_shape = self.patch_embed(x)       # [B, H*W, C], [2*C, W]
        x = self.drop_after_pos(x)
        
        outs = []
        for i, stage in enumerate(self.stages):
            # x: [B, H/2*W/2, 2*C],         out: [B, H*W, C]
            x, hw_shape, out, out_hw_shape = stage(x, hw_shape)
            if i in self.out_indices:
                norm_layer = getattr(self, f'norm{i}')
                
                out = norm_layer(out)
                out = out.view(-1, *out_hw_shape,self.num_features[i])\
                              .permute(0, 3, 1,2)\
                              .contiguous()     # [B, C, H, W]
                outs.append(out)
        return outs


        
    def init_weights(self):
        logger = LOGGERS['"initialization"']
       
        if self.init_cfg is None:
            logger.warn(f'No pre-trained weights for {self.__class__.__name__}, training start from scratch')
            for m in self.modules():
                if isinstance(m, nn.Linear):
                    trunc_normal_init(m, std=.02, bias=0.)
                elif isinstance(m, nn.LayerNorm):
                    constant_init(m, 1.0)
        else:
            assert 'checkpoint' in self.init_cfg, f'Only support ' \
                                                  f'specify `Pretrained` in ' \
                                                  f'`init_cfg` in ' \
                                                  f'{self.__class__.__name__} '
            # ckpt(dict): weight and bias about each layer of pre-trained model 
            ckpt = load_checkpoint(path = self.init_cfg.checkpoint, map_location='cpu', logger=logger)                                                  
            _state_dict = ckpt['model'] 
            if self.convert_weights:        # write backbone name front of all layer name in _state_dict
                # supported loading weight from original repo,
                _state_dict = swin_converter(_state_dict) 
            
            state_dict = dict()
            for k, v in _state_dict.items():
                if k.startswith('backbone.'):
                    # if backbone name is written in front of layer name, delete backbone name 
                    state_dict[k[9:]] = v   # len('backbone.') : 9
            
            # strip prefix of state_dict
            if list(state_dict.keys())[0].startswith('module.'):
                # delete `module` if `module` is written in front of layer name 
                state_dict = {k[7:]: v for k, v in state_dict.items()}   # len('module.') : 7

            # interpolate position bias table if needed
            relative_position_bias_table_keys = [
                k for k in state_dict.keys()
                if 'relative_position_bias_table' in k
            ]
            for table_key in relative_position_bias_table_keys:
                table_pretrained = state_dict[table_key]
                table_current = self.state_dict()[table_key]
                L1, nH1 = table_pretrained.size()
                L2, nH2 = table_current.size()
                if nH1 != nH2:  
                    logger.warning(f'Error in loading {table_key}, pass')
                elif L1 != L2:  
                    # resizing
                    S1 = int(L1**0.5)
                    S2 = int(L2**0.5)
                    table_pretrained_resized = F.interpolate(
                        table_pretrained.permute(1, 0).reshape(1, nH1, S1, S1),
                        size=(S2, S2),
                        mode='bicubic')
                    state_dict[table_key] = table_pretrained_resized.view(
                        nH2, L2).permute(1, 0).contiguous()
                
            # load state_dict (nn.module)
            self.load_state_dict(state_dict, False)
        
        
            
def swin_converter(ckpt):
    new_ckpt = dict()

    def correct_unfold_reduction_order(x):
        out_channel, in_channel = x.shape
        x = x.reshape(out_channel, 4, in_channel // 4)
        x = x[:, [0, 2, 1, 3], :].transpose(1,
                                            2).reshape(out_channel, in_channel)
        return x

    def correct_unfold_norm_order(x):
        in_channel = x.shape[0]
        x = x.reshape(4, in_channel // 4)
        x = x[[0, 2, 1, 3], :].transpose(0, 1).reshape(in_channel)
        return x

    for k, v in ckpt.items():
        if k.startswith('head'):
            continue
        elif k.startswith('layers'):
            new_v = v
            if 'attn.' in k:
                new_k = k.replace('attn.', 'attn.w_msa.')
            elif 'mlp.' in k:
                if 'mlp.fc1.' in k:
                    new_k = k.replace('mlp.fc1.', 'ffn.layers.0.0.')
                elif 'mlp.fc2.' in k:
                    new_k = k.replace('mlp.fc2.', 'ffn.layers.1.')
                else:
                    new_k = k.replace('mlp.', 'ffn.')
            elif 'downsample' in k:
                new_k = k
                if 'reduction.' in k:
                    new_v = correct_unfold_reduction_order(v)
                elif 'norm.' in k:
                    new_v = correct_unfold_norm_order(v)
            else:
                new_k = k
            new_k = new_k.replace('layers', 'stages', 1)
        elif k.startswith('patch_embed'):
            new_v = v
            if 'proj' in k:
                new_k = k.replace('proj', 'projection')
            else:
                new_k = k
        else:
            new_v = v
            new_k = k

        new_ckpt['backbone.' + new_k] = new_v

    return new_ckpt