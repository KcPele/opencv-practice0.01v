import cv2
import numpy as np


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 10:
            cv2.drawContours(imgContour, cnt, -1, (255, 0,0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objcor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x,y), (x+w,y+h), (0,255,0), 2)


img = cv2.imread("resources/shapes1.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)
imgCanny = cv2.Canny(imgBlur, 50,50)
getContours(imgCanny)
cv2.imshow("Horizontal", imgContour)

cv2.waitKey(0)