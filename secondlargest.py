n=int(input())
A=[]

for i in range(n):
    value=int(input())
    A.append(value)

A.sort(reverse=True)

print(A)

for i in range(n):
    if(A[i]<A[0]):
        print(A[i])
        break




