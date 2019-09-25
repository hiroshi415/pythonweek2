# # blank window
# from tkinter import *
# root1 = Tk()
# root1.mainloop()




# # Creating label
# from tkinter import *
# root1 = Tk()
# theLabel = Label(root1, text="Hello")
# theLabel.pack()
# root1.mainloop()




# # organizing layout
# from tkinter import *
# root = Tk()

# topFrame = Frame(root)
# topFrame.pack()

# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# button1 = Button(topFrame, text="Button 1", fg="red")
# button2 = Button(bottomFrame, text="Button 2", fg="white", bg='black')
# button3 = Button(topFrame, text="Button 3", fg="blue")
# button4 = Button(topFrame, text="Button 4", fg="green")

# button1.pack()
# button2.pack()
# button3.pack()
# button4.pack()

# root.mainloop()





# # organizing layout2
# from tkinter import *
# root = Tk()

# topFrame = Frame(root)
# topFrame.pack(side=LEFT)

# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# button1 = Button(topFrame, text="Button 1", fg="red")
# button2 = Button(bottomFrame, text="Button 2", fg="white", bg='black')
# button3 = Button(topFrame, text="Button 3", fg="blue")
# button4 = Button(topFrame, text="Button 4", fg="green")

# button1.pack(side=LEFT)
# button2.pack(side=RIGHT)
# button3.pack()
# button4.pack(side=BOTTOM)

# root.mainloop()




# # fitting widgets in window
# from tkinter import *
# root = Tk()
# one = Label(root, text='1', bg='red', fg='white')
# one.pack(side=LEFT)
# two = Label(root, text='2', bg='blue', fg='white')
# two.pack(fill=X)
# three = Label(root, text='3', bg='green', fg='white')
# three.pack(side=RIGHT, fill=Y)

# root.mainloop()




# # Grid layout
# from tkinter import *
# root = Tk()

# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Password")

# entry_1 = Entry(root)
# entry_2 = Entry(root)

# label_1.grid(row=0)
# label_2.grid(row=1)

# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)

# root.mainloop()

# # Grid layout aligned text
# from tkinter import *
# root = Tk()

# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Password")

# entry_1 = Entry(root)
# entry_2 = Entry(root)

# label_1.grid(row=0, sticky=W)                    #N, E, S, W
# label_2.grid(row=1, sticky=E)

# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)

# c=Checkbutton(root, text="keep me logged in")
# c.grid(columnspan=2)

# root.mainloop()



# # grid with function
# from tkinter import *

# root = Tk()

# def print_name():
#     print('How are you')

# button = Button(root, text="print in terminal", command=print_name)
# button.pack()

# root.mainloop()




# # mouse click events

# from tkinter import *

# root = Tk()

# def leftClick(event):
#     print('Left')
# def rightClick(event):
#     print('Right')

# frame = Frame(root, width = 300, height = 250)

# frame.bind("<Button-1>", leftClick)
# frame.bind("<Button-3>", rightClick)

# frame.pack()

# root.mainloop()