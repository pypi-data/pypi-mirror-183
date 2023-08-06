import numpy as np
import scipy
from a_cv_imwrite_imread_plus import open_image_in_cv


def np_zoom_in(img, zoom_factor=2.0, *args, **kwargs):
    if zoom_factor <= 1:
        raise ValueError("Zoom factor needs to be > 1 ")
    img = open_image_in_cv(img, channels_in_output=3)
    h, w = img.shape[:2]
    zoom_tuple = (zoom_factor,) * 2 + (1,) * (img.ndim - 2)
    zh = int(np.round(h * zoom_factor))
    zw = int(np.round(w * zoom_factor))
    out = scipy.ndimage.zoom(input=img[:zh, :zw], zoom=zoom_tuple, *args, **kwargs)
    return out
