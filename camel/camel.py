listen = input("camelCase: ")
print("snake_case: ", end="")
for c in listen:
    if c.isupper():
        print(f"_{c.lower()}", end="")
    else:
        print(c, end="")
print("")


