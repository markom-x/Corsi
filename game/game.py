import random
while True:
    try:
        n = int(input("Level: "))
        if n >= 0:
            r = random.randint(1, n)
            while True:
                a = int(input("Guess: "))
                if a < r:
                    print("Too small!")
                elif a > r:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        else:
            continue
    except:
        continue
    break

