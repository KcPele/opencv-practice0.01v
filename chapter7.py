import cv2
import numpy as np
#color dectection

def empty():
    pass
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty)
while True:
    img = cv2.imread("resources/test1.png")

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    print(h_min)


    cv2.imshow("Horizontal", imgHSV)

    cv2.waitKey(1)