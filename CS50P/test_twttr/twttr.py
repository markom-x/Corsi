def main():
    listen = input("Input: ")
    print(shorten(listen))


def shorten(word):
    return f"{word.replace("a", "").replace("A", "").replace("e", "").replace("E", "").replace("i", "").replace("I", "").replace("o", "").replace("O", "").replace("U", "").replace("u", "")}"

if __name__ == "__main__":
    main()
