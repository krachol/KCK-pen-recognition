#!/usr/bin/env python3
from collections import deque
import cv2
import numpy as np
import framework

def main():
    drawing = []

    def add_drawing_point(struct, point):
        (x, y) = point
        print("Adding drawing point..." + str(x))
        last_area = drawing[-1]
        last_area.appendleft(point)

    def add_drawing_area(draw):
        if draw == True:
            print("Start drawing...")
            drawing.append(deque())
        else:
            print("Stop drawing.")

    # Setup callback that fires when 'z' key is clicked 
    framework.on_draw(add_drawing_area)

    while (1):
        img = framework.get_frame()

        # Convert BGR to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = np.array([104, 50, 50])
        upper_blue = np.array([150, 255, 255])

        lower_green = (30, 50, 30)
        upper_green = (100, 255, 255)

        # Threshold the HSV image to get only blue colors
        # mask = cv2.inRange(hsv, lower_blue, upper_blue)
        mask = cv2.inRange(hsv, lower_green, upper_green)

        mask = cv2.erode(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20)))
        mask = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10)))

        mask = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
        mask = cv2.erode(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if radius > 2:
                # Bounding circle
                cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                # Centroid
                cv2.circle(img, center, 5, (0, 0, 255), -1)

                if framework.is_ctrl():
                    add_drawing_point(drawing, center)
                        
        
        # Make drawing
        for drawing_area in drawing:
            for i in np.arange(1, len(drawing_area)):
                if drawing_area[i - 1] is None or drawing_area[i] is None:
                    continue
                
                # thickness = int(np.sqrt(len(drawing_area) / float(i + 1)) * 2.5)
                thickness = 2
                cv2.line(img, drawing_area[i - 1], drawing_area[i], (0, 0, 255), thickness)


        # cv2.imshow('Mask', mask)
        cv2.imshow('Original', img)

        if framework.is_esc():
            break
        framework.get_keys()


if __name__ == '__main__':
    main()
