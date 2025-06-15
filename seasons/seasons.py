from datetime import date, timedelta
import operator, sys, inflect
p = inflect.engine()

def main():
    print(calculate(input("Date of Birth: ")))


def calculate(birth):
    try:
        i = operator.__sub__(date.today(), date.fromisoformat(birth))
        c = int(str(i).replace(" days, 0:00:00", ""))
    except:
        sys.exit("Invalid date")
    m = c*24*60
    return f"{p.number_to_words(m)} minutes".replace(" and ", " ").capitalize()


if __name__ == "__main__":
    main()
