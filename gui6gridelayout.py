from tkinter import *

# def getvals():
#     print(usrvalue.get())
#     print(passvalue.get())

root = Tk()
root.geometry("800x500")
root.title("New Title Here")  # Change the title here

user = Label(root, text="User Name :")
password = Label(root, text="Password :")
user.grid()
password.grid(row=1)

usrvalue = StringVar()
passvalue = StringVar()

usrentry = Entry(root, textvariable=usrvalue)
passentry = Entry(root, textvariable=passvalue)
usrentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
Button(text="Submit",).grid()

root.mainloop()
