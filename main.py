import numpy as np
import cv2, os

# Capturing video
name = input("Your Name? \n")
num_of_photos: int = input("How many photos do you want to take?\n")

try:
    os.chdir("out")
except FileNotFoundError:
    os.mkdir("out")
    os.chdir("chdir")

webcam = cv2.VideoCapture(0)


for x in range(1, int(num_of_photos) + 1):

    file_name = name + str(x) + ".jpg"
    ret, frame = webcam.read()
    print("Took a photo number " + str(x) +": " + str(ret))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(file_name, gray)

webcam.release()
