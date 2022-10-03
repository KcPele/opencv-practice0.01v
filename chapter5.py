import cv2
import numpy as np

img = cv2.imread("resources/test1.png")

cv2.imshow('Black image', img)

cv2.waitKey(0)