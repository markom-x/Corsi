import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        list = ip.split(".")
        try:
            if list[4]:
                return False
        except:
            if 0 <= (int(list[0])) <= 255:
                if 0 <= (int(list[1])) <= 255:
                    if 0 <= (int(list[2])) <= 255:
                        if 0 <= (int(list[3])) <= 255:
                            return True

        return False
    except:
        return False


if __name__ == "__main__":
    main()
