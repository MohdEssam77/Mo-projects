import sys
from PIL import Image, ImageOps
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
file1, ext1 = sys.argv[1].split(".")
file2, ext2 = sys.argv[2].split(".")
if ext1 not in ["jpeg", "png", "jpg"]:
    sys.exit("Invalid input")
if ext2 not in ["jpeg", "png", "jpg"]:
    sys.exit("Invalid output")
if ext1 != ext2:
    sys.exit("Input and output have different extensions")
try:
    image = Image.open(sys.argv[1])
except:
    sys.exit("Input does not exist")
else:
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(image, size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])
