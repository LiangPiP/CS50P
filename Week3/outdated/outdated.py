month=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date=input("Date: ")
        if len(date.split(sep='/'))==3:
            date_mm,date_dd,date_yy=date.split(sep='/')
            date_mm,date_dd,date_yy=int(date_mm),int(date_dd),int(date_yy)
        elif len(date.split(sep=','))==2:
            date_yy=int(date.split(sep=",")[1])
            date_mm=date.split(sep=" ")[0]
            date_dd=int(date.split(sep=",")[0].split(sep=" ")[-1])
            for i in range(12):
                if month[i] == date_mm:
                    break
            date_mm=i+1
        else:
            raise ValueError
        if date_dd>31 or date_dd<1:
            raise ValueError
        if date_mm>12 or date_mm<1:
            raise ValueError
        break
    except ValueError:
        pass


print(f"{date_yy}-{date_mm:02}-{date_dd:02}")