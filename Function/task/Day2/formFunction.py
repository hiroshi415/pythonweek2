user = {}

def check():
    req = input('Do you have a login? (y/n) q to quit: ')
    if req=='y':
        login()
    elif req=='n':
        create_user()
    else:
        exit()

def create_user():
    username = input('Enter a username: ')
    if username in user:
        print('user already exists')
    else:
        user[username] = input('Enter a password: ')
        print('user created')
    login()

def login():
    login_name = input('Enter your login: ')
    password = input('Enter your password: ')
    if login_name in user and user[login_name] == password:
        print('Login success')
    else:
        print('username/password incorrect')

check()
