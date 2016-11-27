import cv2
import template_matching
import framework

if __name__ == '__main__':
    # Read in template image and save its dimensions
    template = cv2.imread('templete.png', 0)

    # List wanted methods
    while (1):
        img = framework.get_frame()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # change it to greyscale,

        # Test all methods
        for name, matched in template_matching.get_next_template_match(img, template):
            cv2.imshow(name, matched)

        if framework.is_esc():
            break;
