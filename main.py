import cv2
import numpy as np

if __name__ == '__main__':
    # Get camera
    cap = cv2.VideoCapture(0)

    # Read in template image and save its dimensions
    template = cv2.imread('templete.png', 0)
    w, h = template.shape[::-1]

    # List wanted methods
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    while (1):

        _, img = cap.read()  # Read frame,
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # change it to greyscale,
        img = cv2.flip(img, 1)  # flip along y axis
        img2 = img.copy()  # and copy to have original stored

        # Test all methods
        for meth in methods:
            method = eval(meth)

            img = img2.copy() # Get original frame

            # Draw rectangle on matches
            # Apply template Matching
            res = cv2.matchTemplate(img, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)

            cv2.rectangle(img, top_left, bottom_right, 255, 2)

            # Show frame
            cv2.imshow(meth, img)

        # Wait on Esc to close
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
