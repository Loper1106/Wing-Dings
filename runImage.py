# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
import cv2 as cv
import sys
import main

# Initializing Camera input
camera = cv.VideoCapture(0)

# Checks if Camera is visible
if not camera.isOpened():
    print("No camera detected...")

# Read until video is completed
while camera.isOpened():
    # Capture frame-by-frame
    ret, frame = camera.read()

    if ret == True:
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
quit()
