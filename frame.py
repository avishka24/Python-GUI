from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("frame")
f1 = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, bg="red", borderwidth=9, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l1 = Label(f1, text="Hii")
l1.pack(pady=150, padx=50)
l2 = Label(f2, text="frame 2")
l2.pack(pady=5)
root.mainloop()











