def main():
    name=input("Input: ")
    print(f"Output: {shorten(name)}")



def shorten(word):
    vowel=["a","e","i","o","u"]
    return "".join(ch for ch in word if ch.lower() not in vowel)


if __name__ == "__main__":
    main()
