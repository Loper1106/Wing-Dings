# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk

global frame
global image_from_frame


def screenshot():
    global frame
    print("Screenshot taken")
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    cv.imwrite("test.png", frame)


def cameraInit():
    global frame
    global image_from_frame
    # Initializing Camera input
    camera = cv.VideoCapture(0)
    # Checks if Camera is visible
    if not camera.isOpened():
        print("No camera detected...")

    # Read until video is completed
    while camera.isOpened():
        # Capture frame-by-frame
        ret, frame = camera.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image_from_frame = Image.fromarray(frame)
        image_from_frame = ImageTk.PhotoImage(image_from_frame)

        return image_from_frame
        # if ret:
        #     image_from_frame = Image.fromarray(frame)
        #     # Display the resulting frame
        #     cv.imshow('Frame', frame)
        #     # Press Q on keyboard to  exit
        #     if cv.waitKey(24) == ord('q'):
        #         break
        # # Break the loop
        # else:
        #     break

    camera.release()
    cv.destroyAllWindows()

# cameraInit()
