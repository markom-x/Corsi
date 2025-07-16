
def main():
     greeting = input("Greeting: ")
     print(value(greeting))

def value(greeting):
    if greeting.casefold().replace(" ", "").rfind("hello") != -1:
        return 0
    elif greeting.casefold().replace(" ", "")[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
