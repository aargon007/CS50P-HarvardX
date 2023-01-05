months = [
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
    date = input("Date: ")
    if "/" in date:
        month, day, year = date.split("/")
        day=day.replace(" ","")
        year=year.replace(" ","")
    elif "," in date:
        date = date.replace(",","")
        month, day, year = date.split(" ")
        if month in months:
            month= months.index(month)+1
    else:
        continue

    try:
        day=int(day)
        month=int(month)
        if int(month)>12 or int(day)>31:
            continue
        else:
            break
    except ValueError:
        continue

print(f"{int(year)}-{int(month):02}-{int(day):02}")