#Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read
#Note: 
#	- Search how to generate QRCode
#	- Search how to read QRCode using webcam
#	- Search how to create and write to text file
#	- Your source code should be in github before Feb 19
#	- Create a demo of your program (1-2 min) and send it directly to my messenger.

import cv2
import pyzbar.pyzbar as pyzbar
import time

# Open Webcam/Camera
Cap = cv2.VideoCapture(0)
Webcam = True

# Scan QR code
while Webcam == True:
    good, Cam = Cap.read()

    DecodeQR = pyzbar.decode(Cam)

    for obj in DecodeQR:
        Info = obj.data
        time.sleep(2)
        Webcam = False

    cv2.imshow("Webcam", Cam)
    cv2.waitKey(1)

File = open("test.txt", "w")
File.write(str(Info) + "\n")

