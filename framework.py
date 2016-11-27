import cv2

# Get camera
cap = cv2.VideoCapture(0)

draw = False
esc = False


def get_frame():
    _, img = cap.read()
    img = cv2.flip(img, 1)  # flip along y axis
    return img


def get_keys():
    global draw
    global esc
    esc = False

    k = cv2.waitKey(1)
    if k == 122:
        draw = not draw
    if k == 27:
        esc = True


def is_esc():
    return esc


def is_ctrl():
    return draw
