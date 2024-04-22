from tkinter import *
root = Tk()
root.geometry("1000x700")
photo = PhotoImage(file="abcd.png")
lab = Label(image=photo)
lab.pack()

root.mainloop()