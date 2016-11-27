import cv2
import numpy as np
import framework

def main():
    drawing = None
    while (1):
        img = framework.get_frame()

        # Convert BGR to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = np.array([104, 50, 50])
        upper_blue = np.array([150, 255, 255])
        lower_green = (29, 86, 6)
        upper_green = (64, 255, 255)

        # Threshold the HSV image to get only blue colors
        # mask = cv2.inRange(hsv, lower_blue, upper_blue)
        mask = cv2.inRange(hsv, lower_green, upper_green)

        mask = cv2.erode(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20)))
        mask = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10)))

        mask = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
        mask = cv2.erode(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(img, img, mask=mask)

        if framework.is_ctrl():
            if drawing is None:
                drawing = mask
            else:
                drawing += mask

        if drawing is None:
            showing_img = mask
        else:
            showing_img = drawing + mask

        showing_img = cv2.erode(showing_img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
        showing_img = cv2.dilate(showing_img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))

        showing_img = cv2.dilate(showing_img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
        showing_img = cv2.erode(showing_img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))

        cv2.imshow('Air draw', showing_img)

        if framework.is_esc():
            break
        framework.get_keys()


if __name__ == '__main__':
    main()
