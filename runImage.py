# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
import cv2 as cv
import sys
import threading

global frame


def screenshot():
    global frame
    print("Screenshot taken")

    cv.imwrite("test.png", frame)


def cameraInit():
    global frame
    # Initializing Camera input
    camera = cv.VideoCapture(0)
    # Checks if Camera is visible
    if not camera.isOpened():
        print("No camera detected...")

    # Read until video is completed
    while camera.isOpened():
        # Capture frame-by-frame
        ret, frame = camera.read()

        if ret:
            # Display the resulting frame
            cv.imshow('Frame', frame)
            # Press Q on keyboard to  exit
            if cv.waitKey(24) == ord('q'):
                break
        # Break the loop
        else:
            break

    camera.release()
    cv.destroyAllWindows()


# cameraInit()
