import numpy as np
import cv2
from hibernation_no1.mmdet.data.transforms.compose import PIPELINES
from hibernation_no1.mmdet.data.transforms.utils import imresize, imrescale



@PIPELINES.register_module()
class Resize:
    """Resize images & bbox & mask.

    This transform resizes the input image to some scale. Bboxes and masks are
    then resized with the same scale factor. If the input dict contains the key
    "scale", then the scale in the input dict is used, otherwise the specified
    scale in the init method is used. If the input dict contains the key
    "scale_factor" (if MultiScaleFlipAug does not give img_scale but
    scale_factor), the actual scale will be computed by image shape and
    scale_factor.

    `img_scale` can either be a tuple (single-scale) or a list of tuple
    (multi-scale). There are 3 multiscale modes:

    - ``ratio_range is not None``: randomly sample a ratio from the ratio \
      range and multiply it with the image scale.
    - ``ratio_range is None`` and ``multiscale_mode == "range"``: randomly \
      sample a scale from the multiscale range.
    - ``ratio_range is None`` and ``multiscale_mode == "value"``: randomly \
      sample a scale from multiple scales.

    Args:
        img_scale (tuple or list[tuple]): Images scales for resizing.
        multiscale_mode (str): Either "range" or "value".
        ratio_range (tuple[float]): (min_ratio, max_ratio)
        keep_ratio (bool): Whether to keep the aspect ratio when resizing the
            image.
        bbox_clip_border (bool, optional): Whether to clip the objects outside
            the border of the image. In some dataset like MOT17, the gt bboxes
            are allowed to cross the border of images. Therefore, we don't
            need to clip the gt bboxes in these cases. Defaults to True.
        backend (str): Image resize backend, choices are 'cv2' and 'pillow'.
            These two backends generates slightly different results. Defaults
            to 'cv2'.
        interpolation (str): Interpolation method, accepted values are
            "nearest", "bilinear", "bicubic", "area", "lanczos" for 'cv2'
            backend, "nearest", "bilinear" for 'pillow' backend.
        override (bool, optional): Whether to override `scale` and
            `scale_factor` so as to call resize twice. Default False. If True,
            after the first resizing, the existed `scale` and `scale_factor`
            will be ignored so the second resizing can be allowed.
            This option is a work-around for multiple times of resize in DETR.
            Defaults to False.
    """

    def __init__(self,
                 img_scale=None,     # must be tuple.
                 keep_ratio=True,
                 bbox_clip_border=True,
                 interpolation='bilinear',
                 override=False):

        if img_scale is None:
            self.img_scale = None
        # img_scale : (width, height)
        else:
            if isinstance(img_scale, list): 
                self.img_scale = img_scale
            else:
                self.img_scale = [img_scale]
       
      
        self.keep_ratio = keep_ratio
        # TODO: refactor the override option in Resize
        self.interpolation = interpolation
        self.override = override
        self.bbox_clip_border = bbox_clip_border

    # TODO: using this
    # def random_select(img_scales):
    #     """Randomly select an img_scale from given candidates.

    #     Args:
    #         img_scales (list[tuple]): Images scales for selection.

    #     Returns:
    #         (tuple, int): Returns a tuple ``(img_scale, scale_dix)``, \
    #             where ``img_scale`` is the selected image scale and \
    #             ``scale_idx`` is the selected index in the given candidates.
    #     """

    #     assert mmcv.is_list_of(img_scales, tuple)
    #     scale_idx = np.random.randint(len(img_scales))
    #     img_scale = img_scales[scale_idx]
    #     return img_scale, scale_idx

    # @staticmethod
    # def random_sample(img_scales):
    #     """Randomly sample an img_scale when ``multiscale_mode=='range'``.

    #     Args:
    #         img_scales (list[tuple]): Images scale range for sampling.
    #             There must be two tuples in img_scales, which specify the lower
    #             and upper bound of image scales.

    #     Returns:
    #         (tuple, None): Returns a tuple ``(img_scale, None)``, where \
    #             ``img_scale`` is sampled scale and None is just a placeholder \
    #             to be consistent with :func:`random_select`.
    #     """

    #     assert mmcv.is_list_of(img_scales, tuple) and len(img_scales) == 2
    #     img_scale_long = [max(s) for s in img_scales]
    #     img_scale_short = [min(s) for s in img_scales]
    #     long_edge = np.random.randint(
    #         min(img_scale_long),
    #         max(img_scale_long) + 1)
    #     short_edge = np.random.randint(
    #         min(img_scale_short),
    #         max(img_scale_short) + 1)
    #     img_scale = (long_edge, short_edge)
    #     return img_scale, None

    # @staticmethod
    # def random_sample_ratio(img_scale, ratio_range):
    #     """Randomly sample an img_scale when ``ratio_range`` is specified.

    #     A ratio will be randomly sampled from the range specified by
    #     ``ratio_range``. Then it would be multiplied with ``img_scale`` to
    #     generate sampled scale.

    #     Args:
    #         img_scale (tuple): Images scale base to multiply with ratio.
    #         ratio_range (tuple[float]): The minimum and maximum ratio to scale
    #             the ``img_scale``.

    #     Returns:
    #         (tuple, None): Returns a tuple ``(scale, None)``, where \
    #             ``scale`` is sampled ratio multiplied with ``img_scale`` and \
    #             None is just a placeholder to be consistent with \
    #             :func:`random_select`.
    #     """

    #     assert isinstance(img_scale, tuple) and len(img_scale) == 2
    #     min_ratio, max_ratio = ratio_range
    #     assert min_ratio <= max_ratio
    #     ratio = np.random.random_sample() * (max_ratio - min_ratio) + min_ratio
    #     scale = int(img_scale[0] * ratio), int(img_scale[1] * ratio)
    #     return scale, None

    def _random_scale(self, results):
        """Randomly sample an img_scale according to ``ratio_range`` and
        ``multiscale_mode``.

        If ``ratio_range`` is specified, a ratio will be sampled and be
        multiplied with ``img_scale``.
        If multiple scales are specified by ``img_scale``, a scale will be
        sampled according to ``multiscale_mode``.
        Otherwise, single scale will be used.

        Args:
            results (dict): Result dict from :obj:`dataset`.

        Returns:
            dict: Two new keys 'scale` and 'scale_idx` are added into \
                ``results``, which would be used by subsequent pipelines.
        """
     
        if len(self.img_scale) == 1:
            scale, scale_idx = self.img_scale[0], 0
        else:
            raise NotImplementedError

        results['scale'] = scale
        results['scale_idx'] = scale_idx

    def _resize_img(self, results):
        """Resize images with ``results['scale']``."""

        
        for key in results.get('img_fields', ['img']):
            if self.keep_ratio:
                img, scale_factor = imrescale(results[key],
                                              results['scale'],
                                              return_scale=True,
                                              interpolation=self.interpolation)
                # the w_scale and h_scale has minor difference
                # a real fix should be done in the mmcv.imrescale in the future
                new_h, new_w = img.shape[:2]
                h, w = results[key].shape[:2]
                w_scale = new_w / w
                h_scale = new_h / h
            else:
                img, w_scale, h_scale = imresize(
                    results[key],
                    results['scale'],
                    return_scale=True,
                    interpolation=self.interpolation)
            results[key] = img

            scale_factor = np.array([w_scale, h_scale, w_scale, h_scale],
                                    dtype=np.float32)
            results['img_shape'] = img.shape
            # in case that there is no padding
            results['pad_shape'] = img.shape
            results['scale_factor'] = scale_factor
            results['keep_ratio'] = self.keep_ratio

    def _resize_bboxes(self, results):
        """Resize bounding boxes with ``results['scale_factor']``."""
        for key in results.get('bbox_fields', []):
            bboxes = results[key] * results['scale_factor']
            if self.bbox_clip_border:
                img_shape = results['img_shape']
                bboxes[:, 0::2] = np.clip(bboxes[:, 0::2], 0, img_shape[1])
                bboxes[:, 1::2] = np.clip(bboxes[:, 1::2], 0, img_shape[0])
            results[key] = bboxes

    def _resize_masks(self, results):
        """Resize masks with ``results['scale']``"""
        for key in results.get('mask_fields', []):
            if results[key] is None:
                continue
            if self.keep_ratio:
                results[key] = results[key].rescale(results['scale'])
            else:
                results[key] = results[key].resize(results['img_shape'][:2])

    def _resize_seg(self, results):
        """Resize semantic segmentation map with ``results['scale']``."""
        for key in results.get('seg_fields', []):
            if self.keep_ratio:
                gt_seg = imrescale(
                    results[key],
                    results['scale'],
                    interpolation='nearest')
            else:
                gt_seg = imresize(
                    results[key],
                    results['scale'],
                    interpolation='nearest')
            results[key] = gt_seg


    def __call__(self, results):
        """Call function to resize images, bounding boxes, masks, semantic
        segmentation map.

        Args:
            results (dict): Result dict from loading pipeline.

        Returns:
            dict: Resized results, 'img_shape', 'pad_shape', 'scale_factor', \
                'keep_ratio' keys are added into result dict.
        """
        
        
        if 'scale' not in results:
            if 'scale_factor' in results:                
                img_shape = results['img'].shape[:2]
                scale_factor = results['scale_factor']
                assert isinstance(scale_factor, float)
                results['scale'] = tuple(
                    [int(x * scale_factor) for x in img_shape][::-1])
            else:
                self._random_scale(results)
        else:
            if not self.override:
                assert 'scale_factor' not in results, (
                    'scale and scale_factor cannot be both set.')
            else:
                results.pop('scale')
                if 'scale_factor' in results:
                    results.pop('scale_factor')
                self._random_scale(results)

        # resizing image, bbox, mask, polygons 
        self._resize_img(results)
        self._resize_bboxes(results)
        self._resize_masks(results)
        self._resize_seg(results)
        return results

    def __repr__(self):
        repr_str = self.__class__.__name__
        repr_str += f'(img_scale={self.img_scale}, '
        repr_str += f'keep_ratio={self.keep_ratio}, '
        repr_str += f'bbox_clip_border={self.bbox_clip_border})'
        return repr_str
    
    
