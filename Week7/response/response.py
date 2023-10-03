import validators

def main():
    print(convert(input("What's your email address? ")))

def convert(s):
    if validators.email(s):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()