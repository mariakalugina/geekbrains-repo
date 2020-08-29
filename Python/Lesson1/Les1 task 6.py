a = input("Enter a ")
if (type(float(a)) == float) and (float(a)>0):
    a=float(a)
    b = input("Enter b ")
    if (type(float(b)) == float) and (float(b)>0):
        n=1
        b=float(b)
        kmeveryday=a
        while kmeveryday < b:
            n=n+1
            kmeveryday = kmeveryday*1.1
            #print(f"{n} {kmeveryday}")
        print(f"It was on the {n} day")
    else: print("Uncorrect format")
else: print("Uncorrect format")