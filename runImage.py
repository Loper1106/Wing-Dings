# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk

# Global Variables
global camera
global frame


def screenshot():
    global frame
    print("Screenshot taken")
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    cv.imwrite("test.png", frame)


def cameraInit():
    global camera
    # Initializes Camera
    camera = cv.VideoCapture(0)
    if not camera.isOpened():
        print("No Camera Detected...")
    else:
        print("Camera Initiated!")


def grabFrame():
    global camera
    global frame
    if camera.isOpened():
        # Capture Frame-by-frame
        ret, frame = camera.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image_from_frame = Image.fromarray(frame)
        image_from_frame = ImageTk.PhotoImage(image_from_frame)
        return image_from_frame
