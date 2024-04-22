from tkinter import *
root = Tk()
root.geometry("800x500")
# Title Change this code
root.title("Abhishek GUI App Button")
def hello():
    print("Click Me Bro")

frame = Frame(root,borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")
b1 = Button(frame,fg="red", text="Print Now", command=hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame,fg="red", text="Print Now")
b2.pack(side=LEFT)

b3 = Button(frame,fg="red", text="Print Now")
b3.pack(side=LEFT)

root.mainloop()