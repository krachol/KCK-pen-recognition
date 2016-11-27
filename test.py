import cv2
import framework
import numpy as np
import template_matching

if __name__ == '__main__':
    template = cv2.imread('images/microsoft_pen.png', 0)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fgbg = cv2.createBackgroundSubtractorMOG2()

    # List wanted methods
    while (1):

        img = framework.get_frame()
        original = img

        img = fgbg.apply(img)
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        img = cv2.medianBlur(img, 5)

        canny = cv2.Canny(img, 100, 200)
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        thres1 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        _, thres2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        (_, cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow('Test', canny)

        cv2.imshow('Threshold', thres2)
        for c in cnts:
            cv2.drawContours(img, [c], -1, (0, 255, 0), 2)

        cv2.imshow('counturs', img)

        for name, matched in template_matching.get_next_template_match(img, template, original):
            cv2.imshow(name, matched)

        if framework.is_esc():
            break
