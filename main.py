from tkinter import *
from PIL import Image, ImageTk

screen = Tk()
screen.title("ChickieWings By: Ben Loper")
screen.geometry("800x800")


def screenshot():
    print("Screenshot taken")


def main():
    window = Label(screen, image="")
    window.pack()

    screencap = Button(screen, text="Take Picture", command=screenshot)
    screencap.pack(side=BOTTOM)

    screen.mainloop()


if __name__ == '__main__':
    main()

quit()
