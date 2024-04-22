from tkinter import *
root = Tk()
root.geometry("800x500")
# Title Change this code
root.title("Abhishek GUI App Frame")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")
f2 = Frame(root, borderwidth=8, bg="gray",relief=SUNKEN)
f2.pack(side=TOP, fill="x")
l = Label(f1, text="Project Tkinter - Pycharm")
l.pack(pady=142)

l = Label(f2, text="Project Tkinter - Pycharm",font="Helvetica 16 bold")
l.pack()

root.mainloop()