from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("1000x1000")
root.title("GUI")

para = Label(text="AVISHKA", bg="white", fg="blue", padx=100, pady=100, font="poppins 30 bold")
para.pack()
photo = Image.open("haert.jpg")
image = ImageTk.PhotoImage(photo)
image_label = Label(image = image)
image_label.pack()
root.mainloop()















# text-adds text
# bd - background
# fg - foreground
# font-sets the font
# padx -x paading
# pady - y paddign
# relief - border styling - SUNKEN,RAISED,GROOVE,RIDGE
# pack option-
# anchor =
# side - TOP,bottom,left,right
# fill - X  Y