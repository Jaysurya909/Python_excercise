def checker(n):
    if len(n)>8:
        print("Very strong")
    elif len(n)>5 and len(n)<8:
        print("Moderate")
    elif len(n)>3 and len(n)<5:
        print("Weak")
    else:
        print("Very weak")


checker("noob")    