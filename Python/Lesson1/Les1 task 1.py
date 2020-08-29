example_float=0.1
print(example_float)
example_int = 123
print(example_int)
example_str="Masha"
print(example_str)
example_bool=False
print(example_bool)

name = input("Enter your name ")
print(f"Hello, {name}")
age = input("Enter you age(0-100) ")
if type(int(age)) == int:
    age = int(age)
    print(f"You age is {age}")
    salary = input("Enter your salary (float) ")
    if type(float(age)) == float:
        print(f"Now I know your salary {salary} $")

else: print("Uncorrect format")
