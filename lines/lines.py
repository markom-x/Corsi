import sys
a = 0
i = 0
for arg in sys.argv:
    a += 1

if a < 2:
    sys.exit("Too few command-line arguments")
elif a >2:
    sys.exit("Too many command-line arguments")
elif '.py' not in sys.argv[1]:
    sys.exit("Not a Python file")
else:
    try:
        with open(f"{sys.argv[1]}") as file:
            for line in file:
                if line.lstrip().startswith('#'):
                    i = i
                elif line.lstrip() == '':
                    i = i
                else:
                    i += 1
            print(i)
    except FileNotFoundError:
        sys.exit("File does not exist")


