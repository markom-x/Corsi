import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    i = 0
    list = re.findall(r"[\s,\.]?(um[\s,\.])|um$", s, re.IGNORECASE)
    for e in list:
        i += 1
    return i

if __name__ == "__main__":
    main()
