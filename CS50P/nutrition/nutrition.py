listen = input("Item: ").casefold()
fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "honeydew": "90",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80",
}

for fruit in fruits:
    if listen == fruit:
        print(f"Calories: {fruits[fruit]}")
