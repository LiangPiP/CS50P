input=input("Input: ")
vowel=["a","e","i","o","u"]
print("Output: ",end="")
for c in input:
    if c.lower() not in vowel:
        print(c,end="")
