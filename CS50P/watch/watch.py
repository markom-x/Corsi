import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        m = re.match(
            r"^<iframe\s?.+(?:https?://www\.|https?://)youtube\.com/embed/(\w+).+\</iframe>$", s)
        return f"https://youtu.be/" + m.group(1)
    except:
        return "None"




if __name__ == "__main__":
    main()
