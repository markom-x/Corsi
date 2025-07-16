while True:
    try:
        listen = input("Fraction: ").split('/')
        X = int(listen[0])
        Y = int(listen[1])
        if X <= Y:
            fuel = X / Y * 100
            if 1 < fuel < 99:
                print(f"{fuel:.0f}%")
            elif fuel <= 1:
                print("E")
            elif fuel >= 99:
                print("F")
            break
        else:
            continue

    except ValueError:
        continue
    except ZeroDivisionError:
        continue



