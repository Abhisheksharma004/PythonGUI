from tkinter import *


root = Tk()
root.geometry("644x344")
root.title("Abhishek GUI App")
# root.configure(bg="red")

Label(root, text="Wel Come My Application", font="Arial 16 bold", pady=15, fg="red").grid(row=0, column=3)
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emg = Label(root, text="Emergency Contact")
paymode = Label(root, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emg.grid(row=4, column=2)
paymode.grid(row=5, column=2)

nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
emgval = StringVar()
paymodeval = StringVar()

nameentry = Entry(root, textvariable=nameval)
phoneentry = Entry(root, textvariable=phoneval)
genderentry = Entry(root, textvariable=genderval)
emgentry = Entry(root, textvariable=emgval)
paymodeentry = Entry(root, textvariable=paymodeval)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emgentry.grid(row=4, column=3)
paymodeentry.grid(row=5, column=3)



root.mainloop()
