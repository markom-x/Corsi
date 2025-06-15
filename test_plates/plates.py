def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    num = False
    for c in s:
        i = i+1
        if i <= 2:
            if c.isdigit():
                return False
            else:
                continue
        if i > 2 and i <= 6:
            if c.isdigit():
                num = True
                if i == 3 and c == '0':
                    return False
                else:
                    continue
            elif c.isalnum():
                if num is True:
                    return False
                else:
                    continue
                num = False
            else:
                return False

        else:
            return False
    if i < 2:
        return False

    return True

if __name__ == "__main__":
    main()
