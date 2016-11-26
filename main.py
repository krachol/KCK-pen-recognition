import cv2
import template_matching

if __name__ == '__main__':
    # Get camera
    cap = cv2.VideoCapture(0)

    # Read in template image and save its dimensions
    template = cv2.imread('templete.png', 0)

    # List wanted methods
    while (1):
        _, img = cap.read()  # Read frame,
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # change it to greyscale,
        img = cv2.flip(img, 1)  # flip along y axis

        # Test all methods
        for name, matched in template_matching.get_next_template_match(img, template):
            cv2.imshow(name, matched)

        # Wait on Esc to close
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
