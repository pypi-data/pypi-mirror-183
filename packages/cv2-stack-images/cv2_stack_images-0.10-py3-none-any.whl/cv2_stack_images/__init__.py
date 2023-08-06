import cv2
import numpy as np
from a_cv_imwrite_imread_plus import open_image_in_cv, save_cv_image
from a_cv2_easy_resize import add_easy_resize_to_cv2

add_easy_resize_to_cv2()


def concat2images(img1, img2, width=None, height=None, save_path=None):
    numpy_concat1 = None
    if type(width) == type(height):
        raise ValueError("width / height -> one must be int, the other None")
    imageeins = open_image_in_cv(img1, channels_in_output=3).copy()
    imagezwei = open_image_in_cv(img2, channels_in_output=3).copy()

    if width is not None:
        imageeins = cv2.easy_resize_image(
            imageeins,
            width=width,
            height=None,
            percent=None,
            interpolation=cv2.INTER_AREA,
        )
        imagezwei = cv2.easy_resize_image(
            imagezwei,
            width=width,
            height=None,
            percent=None,
            interpolation=cv2.INTER_AREA,
        )
        numpy_concat1 = np.concatenate((imageeins, imagezwei), axis=0)

    elif height is not None:
        imageeins = cv2.easy_resize_image(
            imageeins,
            width=None,
            height=height,
            percent=None,
            interpolation=cv2.INTER_AREA,
        )
        imagezwei = cv2.easy_resize_image(
            imagezwei,
            width=None,
            height=height,
            percent=None,
            interpolation=cv2.INTER_AREA,
        )
        numpy_concat1 = np.concatenate((imageeins, imagezwei), axis=1)
    if save_path is not None:
        save_cv_image(save_path, numpy_concat1)
    return numpy_concat1


