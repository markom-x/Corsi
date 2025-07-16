import re

name = input("Enter the name").strip()

if re.search(r"^\w+@.\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


