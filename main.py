import runImage
from tkinter import *
from PIL import Image, ImageTk
import threading

screen = Tk()
screen.title("ChickieWings By: Ben Loper")
screen.geometry("800x800")


def main():
    picture = ImageTk.PhotoImage(runImage.image_from_frame)
    window = Label(screen, image=picture)
    window.pack()

    screencap = Button(screen, text="Take Picture", command=lambda: runImage.screenshot())
    screencap.pack(side=BOTTOM)

    screen.mainloop()


if __name__ == '__main__':
    threading.Thread(target=runImage.cameraInit())
    threading.Thread(target=main())
