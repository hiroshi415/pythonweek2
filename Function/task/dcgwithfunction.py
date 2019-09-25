
def findGCD(a,b):
    x = []
    y = []
    for i in range(1, a):
        if(a%i == 0):
            x.append(i)
    print(x)
    for j in range(1, b):
        if(b%j == 0):
            y.append(j)
    print(y)
    # if a>b:
    #     for k in range(len(x)-1, 0, k-=0):
    #         for l in range(len(y)-1, 0, l-=1):
    #             if(x[k] == y[l]):
    #                 return x[k]

    # elif b>a:
    #     for q in range(len(y)-1, 0, q-1):
    #         for w in range(len(x)-1, 0, w-1):
    #             if(x[q] == y[w]):
    #                 return y[q]


print(findGCD(28, 16))
