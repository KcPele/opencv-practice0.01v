import cv2
import numpy as np

img = cv2.imread("resources/test1.png")

imgHor = np.hstack((img, img))

cv2.imshow("Horizontal", imgHor)

cv2.waitKey(0)