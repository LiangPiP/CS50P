import sys
import csv

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as file1:
        reader=csv.DictReader(file1)
        with open(sys.argv[2],'w') as file2:
            fieldnames=['first','last','house']
            writer = csv.DictWriter(file2, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                last,first=row['name'].strip().split(', ')
                house=row['house']
                writer.writerow({'first':first,'last':last,'house':house})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}.csv")

