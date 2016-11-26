import cv2
import numpy as np

if __name__ == '__main__':
    # Get camera
    cap = cv2.VideoCapture(0)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    fgbg = cv2.createBackgroundSubtractorMOG2()

    # List wanted methods
    while (1):

        _, img = cap.read()  # Read frame,
        
        img = fgbg.apply(img)
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # change it to greyscale,
        # img = cv2.flip(img, 1)  # flip along y axis
        # img = cv2.medianBlur(img, 5)

        # canny = cv2.Canny(img, 100, 200)
        # blur = cv2.GaussianBlur(img,(5,5),0)
        # thres1 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        # _, thres2 = cv2.threshold(blur,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        # (_, cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.imshow('Test', canny)


        # cv2.imshow('Threshold', thres2)
        # for c in cnts:
        #     cv2.drawContours(img, [c], -1, (0, 255, 0), 2)

        cv2.imshow('test', img)

        # Wait on Esc to close
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
