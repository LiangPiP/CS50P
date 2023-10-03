import sys
from tabulate import tabulate
import csv

if len(sys.argv)==1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].rstrip().endswith("csv"):
    sys.exit("Not a CSV file")

lines=[]
try:
    with open(sys.argv[1]) as file:
        print(tabulate(csv.DictReader(file), headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")