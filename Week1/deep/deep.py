print("What is the answer to the Great Question of Life, the Universe and Everything? ",end="")
text=input().lower().strip()
match text:
    case "42"|"forty-two"|"forty two":
        print("Yes")
    case _:
        print("No")