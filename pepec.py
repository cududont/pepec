from tkinter import *
import random

def move():
    x, y = str(random.randrange(1200)), str(random.randrange(800))
    loc = "280x300+" + x + '+' + y
    root.geometry(loc)
    root.after(25, move)

root = Tk()
root.title("lol")
root.geometry("300x300")


img = """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"""

photo = PhotoImage(data=img)
label = Label(root, image=photo)
label.place(x=10, y=10)

label2 = Label(root, text="bop", font=("arial",25, "bold"), fg="black").place(x=100, y=262)

move()


root.mainloop()


