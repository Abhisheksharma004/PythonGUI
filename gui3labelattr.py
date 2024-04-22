from tkinter import *
root = Tk()
root.geometry("1000x700")
# Title Change this code
root.title("Abhishek GUI App")

title_lab = Label(text="Lorem Ipsum is simply dummy text of the printing\n and typesetting industry. Lorem Ipsum has been the industry's \nstandard dummy text ever since the 1500s,\n when an unknown printer took a galley\n of type and scrambled it to make a type specimen book.",bg="red",fg="white",padx=94,pady=100,font="comicsansma 19 bold", borderwidth=3,relief=SUNKEN)

title_lab.pack(side=BOTTOM, anchor="sw", fill='x')


root.mainloop()