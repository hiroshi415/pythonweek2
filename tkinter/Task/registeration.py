from tkinter import *
root = Tk()
root.geometry('500x500')
root.title("Registration Form")
Fullname = StringVar()
Email = StringVar()
var = IntVar()
c = StringVar()
var1 = IntVar()


def database():
    name1 = Fullname.get()
    email = Email.get()
    gender = var.get()
    country = c.get()
    prog = var1.get()


title = Label(root, text="Registration form", width=20, font=("bold", 20))
title.place(x=100, y=53)

# Name
numOneLabel = Label(root, text="Full Name ")
numOneEntry = Entry(root)
numOneLabel.place(x=150, y=93)
numOneEntry.place(x=220, y=93)
emailLabel = Label(root, text="Email ")
emailEntry = Entry(root)
emailLabel.place(x=150, y=123)
emailEntry.place(x=220, y=123)

# Gender
genderLabel = Label(root, text="Gender ")
genderLabel.place(x=150, y=153)
male = Radiobutton(root, text="Male", value="Male")
male.place(x=220, y=153)
female = Radiobutton(root, text="Female", value="Female")
female.place(x=280, y=153)

# Country
variable = StringVar(root)
variable.set("Japan")  # default value
countryLabel = Label(root, text="Country ")
countryLabel.place(x=150, y=183)
country = OptionMenu(root, variable, "Japan", "India", "Vietnam")
country.place(x=220, y=183)
country.config(width=14)

# Checkbox
buttonLabel = Label(root, text="Country ")
buttonLabel.place(x=150, y=213)
checkButton1 = Checkbutton(root, text="Javascript")
checkButton1.place(x=220, y=213)
checkButton2 = Checkbutton(root, text="Python")
checkButton2.place(x=300, y=213)

# Submit
submit = Button(root, text="Submit", bg='red', fg='white')
submit.place(x=180, y=243)
submit.config(width=20)

root.mainloop()
