
from os import scandir
import cv2

# reading image
# img = cv2.imread("resources/test1.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

#reading video
# cap = cv2.VideoCapture("resources/KcPele.mp4")

# while True:
#     succes, vImg = cap.read()
#     cv2.imshow("Video", vImg)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#usinf webcam
cam = cv2.VideoCapture(0)

while True:
    succes, vCam = cam.read()
    cv2.imshow("Video", vCam)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
