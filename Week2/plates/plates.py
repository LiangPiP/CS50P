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
    if not s[0:-1].isalnum():
        return False

    for i in range(2,len(s)):
        if not ("A"<=s[i]<="Z"):
            break

    index_lnumber=i
    if s[index_lnumber]=="0":
        return False

    for i in range(i,len(s)):
        if ("A"<=s[i]<="Z"):
            break
    if i !=len(s)-1:
        return False

    return True


main()
