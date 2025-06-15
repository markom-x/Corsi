try:
    items = {}
    while True:
        listen = input().casefold().upper()
        if listen in items:
            items[listen] += 1
        else:
            items[listen] = 1



except EOFError:
    for item in sorted(items):
        print(items[item], item)
