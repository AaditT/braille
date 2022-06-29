# June 28, 2022
# This is an example file showcasing a potential application of the braille model
# Below code uses the opencv module to take a photo and convert any text from the photo to braille

import braille
import cv2

def imgShow():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        cv2.imshow('Detect Image', img)
        if cv2.waitKey(1) == 27:
            print("image taken")
            cv2.imwrite("test.jpg",img)
            if braille.imageToBraille("test.jpg") == "":
                print("Image not recognized")
            break
    cv2.destroyAllWindows()

imgShow()
