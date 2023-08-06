import math
from typing import Union
from a_cv_imwrite_imread_plus import open_image_in_cv, save_cv_image
from create_empty_image import create_new_image
from cv2watermark import (
    merge_image_percentage_width,
)


def create_collage(
    lst: list,
    width: int = 1000,
    background: tuple = (255, 0, 0),
    save_path: Union[None, str] = None,
):
    picli = math.floor(math.sqrt(len(lst)))
    height = width
    stepsw = width // picli
    stepsh = height // picli
    collage = create_new_image(width=width, height=height, color=background)
    collage = open_image_in_cv(collage, channels_in_output=4)
    c = 0
    perc = 100 / picli
    for i in range(0, width, stepsw):
        for j in range(0, height, stepsh):
            try:
                i2 = open_image_in_cv(lst[c], channels_in_output=4)
            except Exception:
                break
            try:
                collage = merge_image_percentage_width(
                    back=collage,
                    front=i2,
                    x=j,
                    y=i,
                    front_percentage_width=perc,
                    save_path=None,
                )
            except Exception as fe:
                print(fe)
                continue

            c += 1
    if save_path is not None:
        save_cv_image(save_path, collage)
    return collage

