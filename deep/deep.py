answer = input ("What is the Answer to the Great Question of Life, the Universe, and Everything?").casefold().replace(" ", "")

match answer:
    case "42":
        print ("Yes")
    case "fortytwo":
        print ("Yes")
    case "forty-two":
        print ("Yes")
    case _:
        print ("No")
