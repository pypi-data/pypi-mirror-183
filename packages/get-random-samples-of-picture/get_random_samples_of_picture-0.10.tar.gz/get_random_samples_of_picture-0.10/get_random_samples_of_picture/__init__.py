import os
import random

import cv2
from a_cv_imwrite_imread_plus import open_image_in_cv, save_cv_image
from a_cv2_easy_resize import add_easy_resize_to_cv2

add_easy_resize_to_cv2()


def cropimage(img, coords):
    return img[coords[1] : coords[3], coords[0] : coords[2]].copy()


def get_random_samples(
    img, width=100, heigth=100, samples=1, save_folder=None, prefix="", zfill=8
):
    img = open_image_in_cv(img)
    if img.shape[1] < width * 4:
        img = cv2.easy_resize_image(
            img,
            width=width * 4,
            height=None,
            percent=None,
            interpolation=cv2.INTER_AREA,
        )
    if img.shape[0] < heigth * 4:
        img = cv2.easy_resize_image(
            img,
            width=None,
            height=heigth * 4,
            percent=None,
            interpolation=cv2.INTER_AREA,
        )
    maxwidth = img.shape[1] - width - 2
    maxheight = img.shape[0] - heigth - 2
    allcrops = []
    for _ in range(samples):
        heightuse = maxheight * 2
        while heightuse > maxheight:
            heightuse = random.randrange(1, img.shape[0])

        widthuse = maxwidth * 2
        while widthuse > maxwidth:
            widthuse = random.randrange(1, img.shape[1])

        pici = cropimage(
            img, (widthuse, heightuse, widthuse + width, heightuse + heigth)
        )
        allcrops.append(pici.copy())
    if save_folder is not None:
        for ini, pi in enumerate(allcrops):
            save_cv_image(
                os.path.join(save_folder, str(prefix) + str(ini).zfill(zfill) + ".png"),
                pi,
            )

    return allcrops

