sec = input("Enter time in sec. It is integer type");
if type(int(sec)) == int:
    sec = int(sec)
    min = sec // 60
    sec = sec % 60
    hour = min // 60
    min = min % 60
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"
    if hour < 10:
        hour = f"0{hour}"
    print(f"The time is {hour}:{min}:{sec}")
else: print("Uncorrect format")


