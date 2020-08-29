income = input("Enter income ")
if type(float(income)) == float:
    expences = input("Enter expences ")
    if type(float(expences)) == float:
        income = float(income)
        expences = float(expences)
        profit = income - expences
    if profit > 0:
        profitability = income/profit
        print(f"The profitability {profitability:.2f} ")
        numberofpeople = input("Enter number of employees. It is an integer ")
        if type(int(numberofpeople)) == int:
            numberofpeople=int(numberofpeople)
            profitPeople = income / numberofpeople
            print(f"Income for per employee is {profitPeople:.2f}")
        else: print("Uncorrect format")
    else: print("I am sorry. Your profit <=0  ")
else: print("Uncorrect format")