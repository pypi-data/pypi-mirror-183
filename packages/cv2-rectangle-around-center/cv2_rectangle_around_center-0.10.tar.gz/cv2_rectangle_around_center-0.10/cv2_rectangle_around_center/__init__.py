import cv2
from a_cv_imwrite_imread_plus import open_image_in_cv, save_cv_image


def _get_coords(center, width, height):
    allpoints = (
        [center[0], center[1]],
        [center[0] + width, center[1]],
        [center[0] + width, center[1] + height],
        [center[0], center[1] + height],
    )
    return allpoints


def line_rectangle_center(
    image,
    center=(50, 100),
    width=50,
    height=100,
    thickness=3,
    color1=(255, 0, 0),
    color2=(255, 0, 0),
    color3=(255, 0, 0),
    color4=(255, 0, 0),
    save_path=None,
):
    allpoints = _get_coords(center, width, height)
    img = open_image_in_cv(image).copy()
    print(allpoints)

    cv2.line(
        img,
        tuple(allpoints[0]),
        tuple(allpoints[1]),
        tuple(reversed(color1)),
        thickness,
    )
    cv2.line(
        img,
        tuple(allpoints[1]),
        tuple(allpoints[2]),
        tuple(reversed(color2)),
        thickness,
    )
    cv2.line(
        img,
        tuple(allpoints[2]),
        tuple(allpoints[3]),
        tuple(reversed(color3)),
        thickness,
    )
    cv2.line(
        img,
        tuple(allpoints[3]),
        tuple(allpoints[0]),
        tuple(reversed(color4)),
        thickness,
    )
    if save_path is not None:
        save_cv_image(save_path, img)
    return img


def rectangle_center(
    image,
    center=(50, 100),
    width=50,
    height=100,
    thickness=3,
    color=(255, 0, 0),
    save_path=None,
):
    allpoints = _get_coords(center, width, height)
    img = open_image_in_cv(image).copy()
    imi = cv2.rectangle(
        img,
        allpoints[0],
        allpoints[2],
        tuple(reversed(color)),
        thickness,
    )
    if save_path is not None:
        save_cv_image(save_path, imi)
    return imi


