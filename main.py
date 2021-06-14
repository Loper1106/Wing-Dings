import runImage
from tkinter import *
from PIL import Image, ImageTk
import threading

screen = Tk()
screen.title("ChickieWings By: Ben Loper")
screen.geometry("800x800")


def main():
    window = Label(screen, image="")
    window.pack()

    screencap = Button(screen, text="Take Picture", command=lambda: runImage.screenshot())
    screencap.pack(side=BOTTOM)

    threading.Thread(target=runImage.cameraInit())

    screen.mainloop()


if __name__ == '__main__':
    main()
