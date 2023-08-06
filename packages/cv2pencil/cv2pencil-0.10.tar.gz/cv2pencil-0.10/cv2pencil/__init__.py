import cv2
import numpy as np
from a_cv_imwrite_imread_plus import open_image_in_cv, save_cv_image


def get_pencil_drawing(img, dilate=(7, 7), blur=5, save_diff=None, save_norm=None):
    img = open_image_in_cv(img, channels_in_output=3)

    rgb_planes = cv2.split(img)
    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones(dilate, np.uint8))
        bg_img = cv2.medianBlur(dilated_img, blur)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(
            diff_img,
            None,
            alpha=0,
            beta=255,
            norm_type=cv2.NORM_MINMAX,
            dtype=cv2.CV_8UC1,
        )
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)

    result_diff = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)

    result_diff = open_image_in_cv(
        open_image_in_cv(result_diff, channels_in_output=2), channels_in_output=3
    )
    result_norm = open_image_in_cv(
        open_image_in_cv(result_norm, channels_in_output=2), channels_in_output=3
    )
    if save_diff is not None:
        save_cv_image(save_diff, result_diff)
    if save_norm is not None:
        save_cv_image(save_norm, result_norm)
    return result_diff, result_norm



