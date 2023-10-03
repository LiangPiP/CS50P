import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        for ch in ip.strip().split("."):
            ch = int (ch)
    except ValueError:
        return False

    if re.search(r"^([1-9]|[1-9]\d|1\d{2}|2([0-4]\d|5[0-5]))\.((\d|[1-9]\d|1\d{2}|2([0-4]\d|5[0-5]))\.){2}(\d|[1-9]\d|1\d{2}|2([0-4]\d|5[0-5]))$",ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

