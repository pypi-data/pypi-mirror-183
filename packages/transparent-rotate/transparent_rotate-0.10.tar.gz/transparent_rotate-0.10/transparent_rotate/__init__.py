from scipy import ndimage
from a_cv_imwrite_imread_plus import open_image_in_cv, save_cv_image


def _rotate(img, angle, save_path=None, reshape=False):
    img = open_image_in_cv(img, channels_in_output=4)

    img_45 = ndimage.rotate(img, angle, reshape=reshape)
    if save_path is not None:
        save_cv_image(save_path, img_45)
    return img_45


def rotate_without_adjusting(img, angle, save_path=None):
    return _rotate(img, angle, save_path=save_path, reshape=False)


def rotate_with_adjusting(img, angle, save_path=None):
    return _rotate(img, angle, save_path=save_path, reshape=True)


