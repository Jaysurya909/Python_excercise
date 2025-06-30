# def area(a,b=None):  defualt arguement
#     if(b==None):
#         print("The area of square is",a*a)
#     else:
#         print("The area of rectangle is",a*b)
def area_variable(*y):
    if(len(y)>1):
        print("The area of rectangle is ",y[0]*y[1])
    else:
        print("The area of square is ",y[0]*y[0])


area_variable(3)
 






