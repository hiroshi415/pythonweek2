def rsp():
    player1 = input('What is your name? ')
    player2 = input('What is your opponent name? ')

    player1choice = input(player1 + '! Rock, Scissors, or Paper? ').lower()
    player2choice = input(player2 + '! Rock, Scissors, or Paper? ').lower()

    if(player1choice == player2choice):
        print("It's a tie")

    elif (player1choice == 'rock' and player2choice == 'scissors'):
        print('Rock wins')
    elif (player1choice == 'rock' and player2choice == 'paper'):
        print('Paper wins')

    elif (player1choice == 'scissors' and player2choice == 'paper'):
        print('Scissors wins')
    elif (player1choice == 'scissors' and player2choice == 'rock'):
        print('Rock wins')

    elif (player1choice == 'paper' and player2choice == 'rock'):
        print('Paper wins!')
    elif (player1choice == 'paper' and player2choice == 'scissors'):
        print('Scissors wins!')


def hangman():
    x = input('Enter a word: ').lower()
    ans = ['-']*len(x)

    while '-' in ans:
        letter = input('Guess a letter: ').lower()
        for i in range(len(x)):
            if x[i] == letter:
                print(letter, 'is in index of', i)
                ans[i] = letter.upper()

        print(ans)
    print('Congrats!')


def num_guess():
    import random

    # generate random number
    randnum = random.randint(0, 9)
    count = 1

    # start guessing until guess is the same value of random number
    guess = int(input('guess a number from 0-9: '))
    while guess != randnum:
        if guess > randnum:
            print('guess too big')
            guess = int(input('guess a number: '))
            count += 1

        else:
            print('guess too small')
            guess = int(input('guess a number: '))
            count += 1
    # only finish when guess is correct
    else:
        print('Number was', randnum)
        print('Correct! You have guess in ', count, 'time(s)!')


# # id name salary department position hire date
# import sqlite3
# mydb = sqlite3.connect('TEST.db')
# mycursor = mydb.cursor()

# mycursor.execute('CREATE TABLE IF NOT EXISTS teachers (id INT AUTO_INCREMENT, name VARCHAR(255), salary INT(255), department VARCHAR(255), position VARCHAR(255), hire_date VARCHAR(255))')
# mycursor.execute("INSERT INTO teachers(id, name, salary, department, position, hire_date) VALUES (10, 'hiroshi10', 10000, 'school', 'student', '2019-10-05')")


# mydb.commit()

# # find birthdays
# def find_birth():
#     li = {'hiroshi':'1001/9/4','rekha':'2005/10/01','kotaro':'1999/09/29', 'seiya':'2000/01/01'}
#     print('Whose birthday do you want to find?')
#     for x in li.keys():
#         print(x)
#     name = input('Enter a name: ')

#     print(name,'was born on',li[name.lower()])

# find_birth()


# # Find Even numbers
# def find_even():
#     li = [1,2,3,4,5,6,10,9,54,31]
#     ans=[]
#     for i in range(len(li)):
#         if(li[i]%2==0):
#             ans.append(li[i])
#     print(li)
#     print(ans)
# find_even()

# # sum of all nums
# def sum_all():
#     li = [1,2,3,4,5,6,7,8,9,10]
#     ans = 0
#     for i in range(len(li)):
#         ans += li[i]
#     print(ans)

# sum_all()

# # find from list
# def find_in_list(a,b):
#     li = [2,4,6,8,10]
#     guess = [a,b]
#     print('From list', li)
#     print('Finding...', guess)
#     if(guess[0] in li and guess[1] in li):
#         print(True)
#     else:
#         print(False)
# find_in_list(1,10)


# # compare lists
# def copm_list():
#     a = [1,2,3,4,5,6,7,8,9,10, 15]
#     b = [1,4,8,11,15, 9, 3]
#     print(a)
#     print(b)
#     ans = []
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if b[j] == a[i]:
#                 ans.append(b[j])
#     print(ans)

# copm_list()

# # remove duplicates(two lines)
# def remove_dup():


from tkinter import *
root=Tk()
root.geometry('300x300')

# radiobutton
first = Radiobutton(root)
first.grid(row=3, column=0)
firstLabel = Label(text='First')
firstLabel.grid(row=3, column=1)
second = Radiobutton(root)
second.grid(row=3, column=2)
secondLabel = Label(text='Second')
secondLabel.grid(row=3, column=3)
third = Radiobutton(root)
third.grid(row=3, column=4)
thirdLabel = Label(text='Third')
thirdLabel.grid(row=3, column=5)

root.mainloop()