def lcm(x, y):

   if x > y:
       bigger = x
   else:
       bigger = y

   while(True):
       if((bigger % x == 0) and (bigger % y == 0)):
           lcm = bigger
           break
       bigger += 1

   return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))