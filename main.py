import runImage
from tkinter import *
from PIL import Image, ImageTk
import threading


class Window:

    def __init__(self):
        self.screen = Tk()
        self.screen.title("ChickieWings By: Ben Loper")
        self.screen.geometry("800x800")


def main(frame):
    picture = ImageTk.PhotoImage(frame)
    window = Label(screen.screen, image=picture)
    window.pack()

    screencap = Button(screen.screen, text="Take Picture", command=lambda: runImage.screenshot())
    screencap.pack(side=BOTTOM)

    # screen.after(0, runImage.cameraInit)
    window.mainloop()


if __name__ == '__main__':
    screen = Window()
    camera = runImage.cameraInit()
    main(camera)
