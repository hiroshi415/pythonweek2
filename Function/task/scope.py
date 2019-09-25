list = [10, 20, 30, 40, 50]

print('before function:',list)
def changelist(a):
    a[1] = a[len(a)-1]
    print('inside function:', a)

changelist(list)
print('after function:',list)


def addToList(a):
    global list
    list.append(a)

addToList(100)
print(list)

