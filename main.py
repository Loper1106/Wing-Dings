import runImage
from tkinter import *
from PIL import Image, ImageTk
import threading

global frame


class Window:

    def __init__(self):
        self.screen = Tk()
        self.screen.title("ChickieWings By: Ben Loper")
        self.screen.geometry("800x800")

        self.window = Label(self.screen, image="")
        self.window.pack()
        self.screencap = Button(self.screen, text="Take Picture", command=lambda: runImage.screenshot())
        self.screencap.pack(side=BOTTOM)


def main():
    global frame

    frame = runImage.cameraInit()
    screen.window["image"] = frame

    screen.screen.update()
    return


if __name__ == '__main__':
    screen = Window()
    while 1:
        main()
