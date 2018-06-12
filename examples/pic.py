import braille
import cv2


def imgShow():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        cv2.imshow('Detect Image', img)
        if cv2.waitKey(1) == 27:
            cv2.imwrite("test.jpg",img)
        else: 
            break
    cv2.destroyAllWindows()

def detectImage():
    imgShow()
    braille.imageToBraille("test.jpg")

detectImage()
