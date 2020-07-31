from tkinter import *
from tkinter import ttk, filedialog
import random
from PIL import ImageTk, Image
import os
import shutil

root = Tk()

path = str(os.path.expanduser('~')).replace('\\', '/')
path = os.path.join(path + "/AppData/Local/osu!/Skins/")


def askdir():
    directory = filedialog.askdirectory(initialdir=path, title="Select osu! skin folder")

    box.delete(0, END)
    box.insert(0, str(directory))


def widen():
    directory = box.get()
    skinname = "WIDE " + str(directory).replace(path, "")
    os.chdir(path)
    os.mkdir(skinname)

    newdirectory = os.path.join(path, skinname)
    os.chdir(directory)
    for f in os.listdir('.'):
        if not f.endswith('.png' or '.'):
            try:
                shutil.copy(f, newdirectory)
            except PermissionError:
                pass

    for f in os.listdir('.'):
        if f.endswith('.png'):
            i = Image.open(f)
            height = i.height
            width = round(i.width*2.5)
            try:
                wide = i.resize((width, height))
            except ValueError:
                pass
            imgdir = os.path.join(newdirectory + "/" + f)
            wide.save(imgdir)


# GUI stuff
s = ttk.Style()
s.configure("Pog.TButton", font=("Segoe", 8))

s1 = ttk.Style()
s1.configure("Pog.TEntry", font=("Segoe", 8))

canvas = Canvas(background='black', width=496, height=110)
image = Image.open("resources/wide.jpg")
image = image.resize((500, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
canvas.create_image(248, 55, anchor=CENTER, image=img)
canvas.place(x=0, y=2)

text = Label(text="Enter Skin Directory: ", font=("Segoe", 8))
text.place(x=0, y=125)

box = ttk.Entry(width=60, style='Pog.TEntry')
box.insert(0, str(path))
box.place(x=105, y=125)

b = ttk.Button(text="...", width=2, style='Pog.TButton', command=askdir)
b.place(x=475, y=123)

title = random.choice([" WIDE PUTIN SIMULATOR", " w e l c o m e  t o  o s u !", " the cake is a lie",
                       " poggers in chat", "Widen your osu! skins!"])

wide = ttk.Button(text="WIDEN", width=15, style='Pog.TButton', command=widen)
wide.place(x=235, y=155)

root.resizable(0, 0)
root.geometry("500x200")
root.title(title)
root.iconbitmap("resources/icon.ico")
root.mainloop()
