n = input("Enter n ")
if type(int(n)) == int:
    n = int(n)
    nn = f"{n}{n}"
    nn=int(nn)
    nnn=f"{n}{n}{n}"
    nnn=int(nnn)
    result=n+nn+nnn;
    print("The result is",result)
else: print("Uncorrect format")


