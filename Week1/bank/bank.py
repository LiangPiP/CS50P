print("Greeting: ",end="")
text=input().lstrip().lower()
if text.startswith('hello'):
    print("$0")
elif text.startswith('h'):
    print("$20")
else:
    print("$100")