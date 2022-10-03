import cv2
import numpy as np


img = np.zeros((512, 512, 3))
print(img)
# img[:] = 255,0,0

cv2.line(img, (0,0), (300,300), (0,255,0))
cv2.rectangle(img, (0,0), (230, 123), (0, 234, 21))
cv2.circle(img, (45,113), 20, (23,34,4))
cv2.putText(img, 'Greate', (23,34), cv2.FONT_HERSHEY_DUPLEX, 2, (2,0,34))
cv2.imshow('Black image', img)

cv2.waitKey(0)