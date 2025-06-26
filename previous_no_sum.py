#my updated logic
def sum():
    inp1=int(input("Enter the first number"))
    inp2=int(input("Enter the second number"))

    for i in range(10):
        print(f"The addition of {inp1} and {inp2} is ",inp1+inp2)
        inp1=(inp1+1)
        inp2=(inp2+1)

sum()



#Given two integer numbers
#write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

#Basic actual answer
def sum2():
    prev=0
    for i in range(10):
        print(f"The previous number is {prev} and current number is {i} and addition is",prev+i)
        prev=i

print("The new loop")
sum2()

