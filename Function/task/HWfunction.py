# Addition!
def add(a, b):
    return a+b

# Factorial!


def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

# nth number of Fibonacci!


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# multiplication table


def multable(n):
    for i in range(1, 10):
        print(n, 'x', i, '=', i*n)


# sum of list
def sumList(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + sumList(n[1:])

# Sum of digits


def sumDigits(n):
    if len(str(n)) == 2:
        return int(str(n)[0]) + int(str(n)[1])
    else:
        return int(str(n)[0]) + sumDigits(int(str(n)[1:]))

# harmonic sum (1+(1/2)+(1/3)+...+(1/n))


def harmSum(n):
    if n == 1:
        return 1
    return "{0:.2f}".format(float((1/n)) + float(harmSum(n-1)))


# GCD
def gcd(a, b):
    if(b > a):
        a, b = b, a
    if(a % b == 0):
        return b
    return gcd(b, a % b)
