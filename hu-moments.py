#!/usr/bin/env python3

import cv2
import numpy as np
import argparse

def save_moments(filepath, moments):
    with open(filepath, 'w') as f:
        for m in moments:
            f.write(str(m) + '\n')

def read_moments()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', help='path to image file')
    ap.add_argument('-o', '--output', help='output path to save moments')
    args = vars(ap.parse_args())

    template = cv2.imread(args['image'])
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Find all colors but not black one (0)
    lower = np.array([1])
    upper = np.array([255])

    shapeMask = cv2.inRange(template, lower, upper)
    
    moments = cv2.HuMoments(cv2.moments(shapeMask)).flatten()
    if args['output'] != None:
        save_moments(args['output'], moments)
    else:
        print(moments)

    # Show shape mask to test if it was ok
    # cv2.imshow('Image', shapeMask)
    # cv2.waitKey(0)

if __name__ == '__main__':
    main()