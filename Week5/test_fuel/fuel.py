def main():
    while True:
        try:
            frac=convert(input("Fraction: "))
            break
        except (ValueError,ZeroDivisionError):
            pass

    print(gauge(frac))


def convert(fraction):
    x,y=fraction.split(sep="/")
    x,y=float(x),float(y)
    if y==0:
        raise ZeroDivisionError
    if x>y:
        raise ValueError
    if x!=int(x) or y!=int(y):
        raise ValueError
    return round(x/y*100)




def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()


