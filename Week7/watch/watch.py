import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if search:=re.search(r'^<iframe.*src="https?://(www\.)?youtube\.com/embed/([0-9a-zA-Z]+)".*$',s):
        url=search.group(2)
        return "https://youtu.be/"+url
    else:
        return None



if __name__ == "__main__":
    main()
