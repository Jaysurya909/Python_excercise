#Given two integer numbers,
#write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
c=a*b
if c<=1000:
    print("The product of the two numbers is ",a*b)
else:
    print("The sum of the two numbers is ",a+b)