import random
import sys

while True:
    try:
        n = int(input("Level: "))
        if n<=0:
            raise ValueError
        break
    except ValueError:
        pass

ran=random.randint(1,n)

while True:
    try:
        guess = int(input("Guess: "))
        if n<=0:
            raise ValueError
        if guess<ran:
            print("Too small!")
        elif guess>ran:
            print("Too large!")
        else:
            sys.exit("Just right!")
    except ValueError:
        pass

