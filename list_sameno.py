def check(y=[1,2,3]):
    #for k,i in enumerate(li1):
        if (y[0]==y[-1]):
            return True
        else:
            return False
        

#Ai answer for even shorter programme
def check1(y):
   return y[0] == y[-1]





li1=[99,24,45,333,54,34,32,99]
li2=[88,45,65,33,55,99]

x=check(li1)
print(x)
y=check() # this one using the default values
print(y)
