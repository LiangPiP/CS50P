def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>6 or len(s)<2:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    for ch in s:
        if not ch.isalnum():
            return False

    for i in range(2,len(s)):
        if not ("A"<=s[i].upper()<="Z"):
            break

    index_lnumber=i
    if s[index_lnumber]=="0":
        return False

    for i in range(index_lnumber,len(s)):
        if ("A"<=s[i].upper()<="Z"):
            return False

    return True


if __name__ == "__main__":
    main()