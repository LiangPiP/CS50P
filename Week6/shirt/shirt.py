import sys
from PIL import Image,ImageOps

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

type1,type2=sys.argv[1].split('.')[-1],sys.argv[2].split('.')[-1]
types=['jpg','jpeg','png']
if (
    type1!=type2 or
    type1 not in types or
    type2 not in types
):
    sys.exit("Error type")

shirt = Image.open("shirt.png")

try:
    with Image.open(sys.argv[1]) as img:
        img=ImageOps.fit(img,shirt.size)
        img.paste(shirt,shirt)
        img.save(sys.argv[2])
except FileNotFoundError:
    sys.exit(f"Could not find {sys.argv[1]}")


