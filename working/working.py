import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if m := re.match(r"([0-9]+):?([0-5][0-9])?.AM to ([0-9]+):?([0-5][0-9:])?.PM", s):
        if int(m.group(1)) == 12:
            if int(m.group(3)) == 12:
                if m.group(2):
                    if m.group(4):
                        return f"00:{m.group(2)} to 12:{m.group(4)}"
                    else:
                        return f"00:{m.group(2)} to 12:00"
                else:
                    if m.group(4):
                        return f"00:00 to 12:{m.group(4)}"
                    else:
                        return f"00:00 to 12:00"
            else:
                if m.group(2):
                    if m.group(4):
                        return f"00:{m.group(2)} to {12 + int(m.group(3))}:{m.group(4)}"
                    else:
                        return f"00:{m.group(2)} to {12 + int(m.group(3))}:00"
                else:
                    if m.group(4):
                        return f"00:00 to {12 + int(m.group(3))}:{m.group(4)}"
                    else:
                        return f"00:00 to {12 + int(m.group(3))}:00"

        elif m.group(2):
            if m.group(4):
                if int(m.group(1)) <= 9:
                    return f"0{m.group(1)}:{m.group(2)} to {12 + int(m.group(3))}:{m.group(4)}"
                else:
                    return f"{m.group(1)}:{m.group(2)} to {12 + int(m.group(3))}:{m.group(4)}"
            else:
                return f"{m.group(1)}:{m.group(2)} to {12 + int(m.group(3))}:00"
        elif m.group(4):
            if int(m.group(1)) <= 9:
                return f"0{m.group(1)}:00 to {12 + int(m.group(3))}:{m.group(4)}"
            else:
                return f"{m.group(1)}:00 to {12 + int(m.group(3))}:{m.group(4)}"
        else:
            if int(m.group(1)) <= 9:
                return f"0{m.group(1)}:00 to {12 + int(m.group(3))}:00"
            else:
                return f"{m.group(1)}:00 to {12 + int(m.group(3))}:00"



    elif m := re.match(r"([0-9]+):?([0-5][0-9])?.PM to ([0-9]+):?([0-5][0-9:])?.AM", s):
        if int(m.group(1)) == 12:
            if int(m.group(3)) == 12:
                if m.group(2):
                    if m.group(4):
                        return f"12:{m.group(2)} to 00:{m.group(4)}"
                    else:
                        return f"12:{m.group(2)} to 00:00"
                else:
                    if m.group(4):
                        return f"12:00 to 00:{m.group(4)}"
                    else:
                        return f"12:00 to 00:00"
            else:
                if m.group(2):
                    if m.group(4):
                        return f"12:{m.group(2)} to {12 + int(m.group(3))}:{m.group(4)}"
                    else:
                        return f"12:{m.group(2)} to {12 + int(m.group(3))}:00"
                else:
                    if m.group(4):
                        return f"12:00 to {12 + int(m.group(3))}:{m.group(4)}"
                    else:
                        return f"12:00 to {12 + int(m.group(3))}:00"
        elif m.group(2):
            if m.group(4):
                if int(m.group(3)) <= 9:
                    return f"{12 + int(m.group(1))}:{m.group(2)} to 0{m.group(3)}:{m.group(4)}"
                else:
                    return f"{12 + int(m.group(1))}:{m.group(2)} to {m.group(3)}:{m.group(4)}"
            else:
                if int(m.group(3)) <= 9:
                    return f"{12 + int(m.group(1))}:{m.group(2)} to 0{m.group(3)}:00"
                else:
                    return f"{12 + int(m.group(1))}:{m.group(2)} to {m.group(3)}:00"
        elif m.group(4):
            if int(m.group(3)) <= 9:
                return f"{12 + int(m.group(1))}:00 to 0{m.group(3)}: {m.group(4)}"
            else:
                return f"{12 + int(m.group(1))}:00 to {m.group(3)}: {m.group(4)}"
        else:
            if int(m.group(3)) <= 9:
                return f"{12 + int(m.group(1))}:00 to 0{m.group(3)}:00"
            else:
                return f"{12 + int(m.group(1))}:00 to {m.group(3)}:00"
    else:
        raise ValueError




if __name__ == "__main__":
    main()
