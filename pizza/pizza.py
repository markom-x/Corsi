import sys, csv
from tabulate import tabulate

a = 0
for arg in sys.argv:
    a += 1

if a < 2:
    sys.exit("Too few command-line arguments")
elif a > 2:
    sys.exit("Too many command-line arguments")
elif '.csv' not in sys.argv[1]:
    sys.exit("Not a CSV file")
else:
    try:
        with open(f"{sys.argv[1]}") as file:
            table = csv.reader(file)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
