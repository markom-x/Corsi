names = []
i = 0
try:
    while True:
        names.insert(i, input("Name: "))
        i += 1
except EOFError:
    print("Adieu, adieu, to ", end="")
    for name in names:
        if names.index(name) - i == -1 and i != 1:
            print(f"and {name}")
        elif i == 1:
            print(f"{name}")
        elif i == 2:
            print(f"{name} ", end="")
        else:
            print(f"{name}, ", end="")


