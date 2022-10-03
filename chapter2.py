
import cv2
import numpy as np

img = cv2.imread("resources/test1.png")
kernel = np.ones((5,5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
#increase the thickness
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
#to make the line thin
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Dilation image", imgEroded)
cv2.waitKey(0)