import sys
from PIL import Image, ImageOps

a = 0
daje = False

for arg in sys.argv:
    a += 1
if a < 3:
    sys.exit("Too few command-line arguments")
elif a > 3:
    sys.exit("Too many command-line arguments")
elif ".jpg" in sys.argv[1].casefold():
    if ".jpg" in sys.argv[2].casefold():
        daje = True
    elif ".jpeg" in sys.argv[2].casefold():
        sys.exit("Input and output have different extensions")
    elif ".png" in sys.argv[2].casefold():
        sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid output")
elif ".jpeg" in sys.argv[1].casefold():
    if ".jpeg" in sys.argv[2].casefold():
        daje = True
    elif ".jpg" in sys.argv[2].casefold():
        sys.exit("Input and output have different extensions")
    elif ".png" in sys.argv[2].casefold():
        sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid output")

elif ".png" in sys.argv[1].casefold():
    if ".png" in sys.argv[2].casefold():
        daje = True
    elif ".jpg" in sys.argv[2].casefold():
        sys.exit("Input and output have different extensions")
    elif ".jpeg" in sys.argv[2].casefold():
        sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid output")
else:
    sys.exit("Invalid input")

if daje == True:
    photo = Image.open(f"{sys.argv[1]}")
    shirt = Image.open("shirt.png")
    mod = ImageOps.fit(photo, shirt.size)
    mod.paste(shirt, shirt)
    mod.save(f"{sys.argv[2]}")



