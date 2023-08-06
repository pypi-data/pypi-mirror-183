import numpy as np
from a_cv_imwrite_imread_plus import open_image_in_cv


def create_new_image_same_size(openimage, color=(0, 0, 0)):
    openimage = open_image_in_cv(openimage)
    color = np.array(list(reversed(color)), dtype=np.uint8)
    emptyimage = color * np.ones(openimage.shape, np.uint8)
    return emptyimage


def create_new_image(width, height, color=(0, 0, 0)):
    color = np.array(list(reversed(color)), dtype=np.uint8)
    emptyimage = color * np.ones((height, width, len(color)), np.uint8)
    return emptyimage


