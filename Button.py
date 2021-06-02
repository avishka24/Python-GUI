from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("button")

def hello():
    print("Hellllo")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack()
b1 = Button(frame, fg="red", text="print now", command=hello)
b1.pack()

root.mainloop()











