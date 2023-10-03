item={}
while True:
    try:
        it=input().upper()
    except EOFError:
        print()
        break

    if it in item:
        item[it]+=1
    else:
        item[it]=1

for s in sorted(list(item)):
    print(f"{item[s]} {s}")