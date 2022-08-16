from logging import root
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Instagram')
# root.geometry('750x580+700+200')


def say(name):
    print("hello " + name)
    

# imgName = Label(root, text=)

img = ImageTk.PhotoImage(Image.open("./watchdog/fox.jpg"))
imLab = Label(image=img)
imLab.pack()

btn = Button(root, text="click", command=lambda:say("shanu"))
btn.pack()

root.mainloop()