import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

## decting faces from images
img = cv2.imread('resources/istockphoto-1313246045-1024x1024.jpg')

imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imggray, 1.1,4)
for(x,y,w,h) in faces:
    print(f'x={x}, y={y}, w={w}, h={h}')
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('Face Detection', img)
cv2.waitKey(0)

##dectectig faces from videos
# cam = cv2.VideoCapture(0)
# while True:
#     success, imgCam = cam.read()
#     imgCamGray = cv2.cvtColor(imgCam, cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(imgCamGray, 1.1, 4)
#     for(x,y,w,h) in faces:
#         cv2.rectangle(imgCam, (x,y), (x+w, y+h), (255,0,34), 1)
#     cv2.imshow('Detecting video faces', imgCam)
#     if cv2.waitKey(1) & 0xFF == ord('q'): break
