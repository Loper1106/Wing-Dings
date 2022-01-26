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
    print("Window Running")

    frame = runImage.grabFrame()
    gui.window["image"] = frame
    gui.screen.update()
    gui.screen.after(0, main)


if __name__ == '__main__':
    gui = Window()
    runImage.cameraInit()

    main()
    gui.screen.mainloop()

