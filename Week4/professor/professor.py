import random


def main():
    score=0
    level=get_level()
    for i in range(10):
        flag=0
        x1,x2=generate_integer(level),generate_integer(level)
        flag=0
        for j in range(3):
            try:
                answer=int(input(str(x1)+' + '+str(x2)+' = '))
                if answer!=x1+x2:
                    raise ValueError
                score+=1
                break
            except ValueError:
                print("EEE")
                flag+=1
                print(flag)
        if flag==3:
            print(str(x1)+' + '+str(x2)+' = '+str(x1+x2))

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n>3 or n<1:
                raise ValueError
            return n
        except ValueError:
            pass


def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
