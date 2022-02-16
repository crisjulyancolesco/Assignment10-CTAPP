import cv2
import pyzbar.pyzbar as pyzbar
import time
from datetime import date
from datetime import datetime

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

# Decode the data
DecodedInfo = Info.decode("utf-8")

# Adding current Time and Date
DateToday = date.today()
DateToday = DateToday.strftime("%m/%d/%y")

TimeNow = datetime.now()
TimeNow = TimeNow.strftime("%H:%M:%S")

# Storing to Text file
File = open("Compilation.txt", "a")
File.write(str(DecodedInfo) + "\n")
File.write("Date Visited: " + DateToday + "\n")
File.write("Time Visited: " + TimeNow + "\n")
File.write("" + "\n") # For spaces after each QR code data