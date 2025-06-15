def main():
    while True:
        try:
            listen = input("Fraction: ")
            print(gauge(convert(listen)))
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

def convert(fraction):
        X, Y = map(int, fraction.split("/"))
        if Y == 0:
            raise ZeroDivisionError
        if X > Y:
            raise ValueError
        return round(X / Y * 100)

def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage}%"
    elif percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"

if __name__ == "__main__":
    main()
