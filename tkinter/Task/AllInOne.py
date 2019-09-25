from tkinter import *
root = Tk()

frame = Frame(root, width=500, height=450)
label = Label(root, text="This is a Label: ")
entry = Entry(root)

label.grid(row=0)
entry.grid(row=0, column=1)


c = Checkbutton(root, text="Check me")
c.grid(columnspan=2)


def leftClick(event):
    print('Left')


def rightClick(event):
    print('Right')


button1 = Button(root, text="Left")
button1.grid(row=2, column=0)
button1.bind('<Button-1>', leftClick)

button2 = Button(root, text="Right")
button2.grid(row=2, column=1)
button2.bind('<Button-1>', rightClick)


root.mainloop()
