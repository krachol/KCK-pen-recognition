#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt

template = cv2.imread('images/pen_better_small.jpg', 0)
dummy = np.zeros((1, 1))

sift = cv2.xfeatures2d.SIFT_create()
bf = cv2.BFMatcher()

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    kp_object, des_object = sift.detectAndCompute(template, None)
    kp_scene, des_scene = sift.detectAndCompute(gray_frame, None)

    matches = bf.knnMatch(des_scene, des_object, k=2)
    good = []
    for m, n in matches:
        if m.distance < .75 * n.distance:
            good.append([m])

    img_result = cv2.drawMatchesKnn(template, kp_object,
                                    frame, kp_scene,
                                    good, dummy, flags=2)
    
    cv2.imshow('Result', img_result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    



