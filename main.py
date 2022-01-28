import runImage
from tkinter import *


class Window:

    def __init__(self):
        self.screen = Tk()
        self.screen.title("ChickieWings By: Ben Loper")
        self.screenWidth = 800
        self.screenHeight = 800
        self.screen.geometry(f"{self.screenWidth}x{self.screenHeight}")

        self.window = Label(self.screen, image="")
        self.window.pack()
        self.screencap = Button(self.screen, text="Take Picture", command=lambda: runImage.screenshot())
        self.screencap.pack(side=BOTTOM)


def loadGui():

    frame = runImage.grabFrame()
    gui.window["image"] = frame
    gui.screen.update()
    gui.screen.after(0, loadGui)


if __name__ == '__main__':
    gui = Window()
    runImage.cameraInit()

    loadGui()
    gui.screen.mainloop()

