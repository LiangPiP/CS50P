while True:
    try:
        x,y=input("Fraction: ").split(sep="/")
        x,y=float((x)),float(int(y))
        if y==0:
            raise ZeroDivisionError
        if x>y:
            raise ValueError
    except (ValueError,ZeroDivisionError):
        continue
    if x!=int(x) or y!=int(y):
        continue
    break

pertentage= round(x/y*100)
if pertentage<=1:
    print("E")
elif pertentage>=99:
    print("F")
else:
    print(f"{pertentage}%")