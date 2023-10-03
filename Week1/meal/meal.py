def main():
    time_str=input("What time is it? ")
    time_float=convert(time_str)
    if 7<=time_float <=8:
        print("breakfast time")
    elif 18<=time_float<=19:
        print("dinner time")
    elif 12<=time_float<=13:
        print("lunch time")

def convert(time):
    x,y=time.split(":")
    return int(x)+int(y)/60


if __name__ == "__main__":
    main()