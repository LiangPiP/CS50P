from datetime import date
import sys
import inflect

def main():
    print(convert(get_date("Date of birth")))


def get_date(s):
    dat=input(f"{s}: ").strip()
    if len(dat.split('-'))!=3:
        sys.exit("Invalid date")
    else:
        try:
            year,month,day=map(int,dat.split('-'))
            return date(year,month,day)
        except (TypeError,ValueError):
            sys.exit("Invalid date")


def convert(date1):
    today=date.today()
    minutes=(today-date1).days*1440

    p=inflect.engine()
    return p.number_to_words(round(minutes),andword="").capitalize()+" minutes"



if __name__ == "__main__":
    main()
