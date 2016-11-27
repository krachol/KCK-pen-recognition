import cv2
import numpy as np

if __name__ == '__main__':
    # Get camera
    cap = cv2.VideoCapture(0)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    fgbg = cv2.createBackgroundSubtractorMOG2()

    # List wanted methods
    while (1):
        _, frame = cap.read()  # Read frame,
        original_frame = frame.copy()

        flipped = cv2.flip(frame, 1)
        blurred = cv2.GaussianBlur(flipped, (11, 11), 0)

        mask = frame
        mask = fgbg.apply(blurred)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # mask = cv2.adaptiveThreshold(mask, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 0)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        
        canny = cv2.Canny(mask, 100, 200)
        
        # (_, cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.imshow('Test', canny)

        # cv2.imshow('Threshold', thres2)
        # for c in cnts:
        #     cv2.drawContours(img, [c], -1, (0, 255, 0), 2)

        cv2.imshow('Frame', original_frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('Canny', canny)

        # Wait on Esc to close
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
