# a = 10
# print('before function:',a)

# def scope():
#     global a
#     a = 15

#     print('inside function:',a)

# scope()
# print('outside after function:', a)


# Recursion
# def recurs():
#     print('hello')
#     recurs()
# recurs()

# import sys 
# sys.setrecursionlimit(500)
# # print(sys.setrecursionlimit())
# i=0

# def recurs():
#     global i
#     i+=1
#     print('Hello', i)
#     recurs()

# recurs()

# def fact(n):
#     print(n)
#     if n == 0:
#         return 1
#     return n*fact(n-1)

# print(fact(5))
# ans = 5
# for i in range(1,5):
#     ans*=i
# print(ans)

'''
# f=lambda a: a*a
# print(f(5))

# f=lambda a,b: a+b
# print(f(10,2))
'''



# def div(a,b):
#     if(a>b):
#         return a/b
#     if(b>a):
#         return b/a


# print(div(4,2))
# print(div(2,4))


# using decorator
def div(a,b):
    print (a/b)

def smart_div(func):
    def inner(a,b):
        if b>a:
            return func(b,a)
    return inner

a = smart_div(div)
a(2,4)