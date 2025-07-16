import random

def main():
    i = 0
    c = 0
    level = get_level()
    while i < 10:
        X = generate_integer(level)
        Y = generate_integer(level)
        e = 0
        while e < 3:
            try:
                a = int(input(f"{X} + {Y} = "))
                if a == X + Y:
                    c += 1
                    break
                else:
                    print("EEE")
                    e += 1
            except:
                print("EEE")
                e += 1

        if e == 3:
            print(f"{X} + {Y} = {X + Y}")

        i += 1
    print(f"Score: {c}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n == 1 or n == 2 or n == 3:
                break
            else:
                continue
        except:
            continue
    return n

def generate_integer(level):
    if level == 1:
        r = random.randint(0, 9)
        return r
    elif level == 2:
        r = random.randint(10, 99)
        return r
    else:
        r = random.randint(100, 999)
        return r



if __name__ == "__main__":
    main()
