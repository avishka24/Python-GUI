from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.geometry("1000x1000")
root.minsize(200, 200)
root.maxsize(1200, 999)
root.title("O")
O = Label(text="Hi Love❤",font="poppins 20")
Avishka = Label(text="I LOVE YOU",fg="red",font=12)
O.pack(anchor="nw")
Avishka.pack()

# tkinter doenot suport jpg format
# photo = PhotoImage(file="haert.jpg")
image = Image.open("haert.jpg")
photo = ImageTk.PhotoImage(image)
heart_label = Label(image=photo)
heart_label.pack()

root.mainloop()