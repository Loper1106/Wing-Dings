from tkinter import *
from PIL import Image, ImageTk

screen = Tk()
screen.title("ChickieWings By: Ben Loper")
screen.geometry("800x800")


def screenshot():
    print("Screenshot taken")


window = Label(screen, image="")
window.pack()

screenshot = Button(screen, text="Take Picture", command=screenshot)
screenshot.pack(side=BOTTOM)

screen.mainloop()
quit()
