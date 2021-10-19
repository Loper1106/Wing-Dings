import runImage
from tkinter import *
from PIL import Image, ImageTk
import threading


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

    screen.screen.after(33, runImage.cameraInit())
    frame = runImage.image_from_frame
    screen.window["image"] = frame

    screen.screen.after(33, main)


if __name__ == '__main__':
    screen = Window()

    main()
    screen.screen.mainloop()
