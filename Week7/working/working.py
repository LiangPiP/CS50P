import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    str=''
    if search:=re.search(
        r"^(([0-9]|1[0-2]):?(\d{2})?) (AM|PM) to (([0-9]|1[0-2]):?(\d{2})?) (AM|PM)$",s.strip()
        ):
        amH,amM=int(search.group(2)),convert_min(search.group(3))
        pmH,pmM=int(search.group(6)),convert_min(search.group(7))
        if search.group(4)=="PM":
            amH=amH%12+12
        else:
            amH=amH%12
        if search.group(8)=="PM":
            pmH=pmH%12+12
        else:
            pmH=pmH%12

        if amM>=60 or pmM>=60:
            raise ValueError
        return f"{amH:02}:{amM:02} to {pmH:02}:{pmM:02}"
    else:
        raise ValueError

def convert_min(min):
    if min==None:
        return 0
    else:
        return int(min)


if __name__ == "__main__":
    main()
