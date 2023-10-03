import sys

if len(sys.argv)==1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too much command-line arguments")

if not sys.argv[1].rstrip().endswith("py"):
    sys.exit("Not a Python file")
flag=0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            if (not line.lstrip().startswith("#")) and line.strip():
                flag+=1
except FileNotFoundError:
    sys.exit("File does not exist")


print(flag)