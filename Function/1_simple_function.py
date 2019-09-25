# def greet():
#     print('good')
#     print('morning')

# greet()
# greet()
# greet()

# def add(a,b):
#     return a + b
# def sub(a,b):
#     return a - b
# def mul(a,b):
#     return a * b
# def div(a,b):
#     return a / b

# print(add(5,4))
# print(sub(5,4))
# print(mul(5,4))
# print(div(8,4))


# def add_sub(a,b):
#     x = a+b
#     y = a-b
#     return x,y

# print(add_sub(10,3))

# def update(x):
#     print(id(x))

# a = 10
# print(id(a),'id of a')

# print('id of x')
# update(14)

# print('a=',a)

# def update(lst):
#     # print(id(lst))

#     lst[1] = 25
#     # print(id(lst))
#     print('x =',lst)

# lst = [10, 20, 30]
# update(lst)
# print('lst:',lst)

# def person(name, age):
#     print(name)
#     print(age)

# person(age = 50, name='JOHN')

# def person(name, age=20):
#     print(name, age)
# person('Hiroshi', 50)

# def person(name, *data):
#     print(name, data)
# person('hiroshi', 83, 'jldak', 7461, 'hlajsd')
# def person2(name, **data):
#     print(name, data)
# person2('hiroshi', age=83, address='jldak', phone=7461, coutry='hlajsd')
# def person3(name, **data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
# person3('hiroshi', age=83, address='jldak', phone=7461, coutry='hlajsd')

print(id(19))