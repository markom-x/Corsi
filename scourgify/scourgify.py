import sys, csv
a = 0
students = []

for arg in sys.argv:
    a += 1

if a < 3:
    sys.exit("Too few command-line arguments")
elif a > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(f"{sys.argv[1]}") as file:
            for line in file:
                students.append(line.replace('"', "").replace(
                    "\n", "").replace(" ", "").split(","))

        with open(f"{sys.argv[2]}", 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["first", "last", "house"])
            for student in students:
                try:
                    writer.writerow([student[1], student[0], student[2]])
                except:
                    continue


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

