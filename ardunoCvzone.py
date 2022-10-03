from time import sleep
from cvzone.SerialModule import SerialObject
from time import sleep
import cv2
arduino = SerialObject()

while True:
    arduino.sendData([1])
    sleep(1)
    arduino.sendData([0])
    sleep(1)