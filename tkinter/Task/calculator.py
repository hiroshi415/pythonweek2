from tkinter import *
root = Tk()
root.geometry('300x300')
root.title("Simple Calculator")


# title
title = Label(root, text="simple calculator")
title.grid(row=0, columnspan=2)

# Number inputs
numOneLabel = Label(root, text="Enter a number: ")
numOneEntry = Entry(root)
numOneLabel.grid(row=1, column=0)
numOneEntry.grid(row=1, column=1)
numTwoLabel = Label(root, text="Enter another number: ")
numTwoEntry = Entry(root)
numTwoLabel.grid(row=2, column=0)
numTwoEntry.grid(row=2, column=1)
# Show answer
ans = Label(root)
ans.grid(row=5, columnspan=2)

# calculate function


def addition():
    c = int(numOneEntry.get()) + int(numTwoEntry.get())
    ans.config(text="Sum is: %s" % c)


def subtraction():
    c = int(numOneEntry.get()) - int(numTwoEntry.get())
    ans.config(text="Difference is: %s" % c)


def multiplication():
    c = int(numOneEntry.get()) * int(numTwoEntry.get())
    ans.config(text="Product is: %s" % c)


def division():
    c = int(numOneEntry.get()) / int(numTwoEntry.get())
    ans.config(text="Quotient is: %s" % c)


# calculate button
add = Button(root, text="Addition", command=addition,
             fg='white', bg='black', width=15)
add.grid(row=3, column=0)
subtract = Button(root, text="Subtraction",
                  command=subtraction, fg='white', bg='red', width=15)
subtract.grid(row=3, column=1)
multiply = Button(root, text="Multiplication",
                  command=multiplication, fg='white', bg='blue', width=15)
multiply.grid(row=4, column=0)
divide = Button(root, text="Division", command=division,
                fg='white', bg='green', width=15)
divide.grid(row=4, column=1)

root.mainloop()
