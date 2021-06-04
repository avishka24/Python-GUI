from tkinter import *

root = Tk()
root.geometry("500x500")

user = Label(root, text="username")
password = Label(root, text="password")
user.grid()
password.grid()

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")

Button(text="submit", command=getvals).grid()
root.mainloop()

# variable classesin tkinter:
# booleanVar, DoubleVar, IntVar, StringVar