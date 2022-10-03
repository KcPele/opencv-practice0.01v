import cv2

img = cv2.imread("resources/test1.png")
print(img.shape)

imgResize = cv2.resize(img, (700, 495))

imgCropped = img[0:200, 200:500]
cv2.imshow('Test image', imgResize)
cv2.imshow('cropedimage', imgCropped)
cv2.waitKey(0)