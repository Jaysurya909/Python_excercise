def leapyear(leap):
    out = None
    if(leap%4==0 and leap%100!=0):
        out=True
    elif(leap%400==0):
        out=True
    return out



year=int(input("Enter the year"))

print(leapyear(year))



