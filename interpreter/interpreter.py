
list = input("Expression: ").rsplit(" ")
x = int(list[0])
y = list[1]
z = int(list[2])

if y == "/" and z == 0:
    print("Invalid expression")
else:
    match y:
        case "+":
            print(float(x + z))
        case "-":
            print(float(x - z))
        case "*":
            print(float(x * z))
        case "/":
            print(float(x / z))
