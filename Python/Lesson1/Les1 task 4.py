n = input("Enter n. It is integer number >0 ")
if (type(int(n)) == int):
    n = int(n)
    if n>=0:
        max=0
        while n > 0:
            if max < n%10:
                max=n%10
            n=n//10
        print(f"Max number is {max}")
    else: print("n has to be >0")
else: print("Uncorrect format")