def main():
    #get time from user
    time=input("What time is it? ")
    time=convert(time)

    #breakfast between 7:00 and 8:00
    if time >=7 and time <=8:
        print("breakfast time")
    #lunch between 12:00 and 13:00
    if time >=12 and time<=13:
        print("lunch time")
    #dinner between 18:00 and 19:00
    if time >=18 and time<=19:
        print("dinner time")

def convert(time):
    #split hour and minutes
    hours, minutes = time.split(":")
    #convert time ino float number
    float_of_minutes=float(minutes)/60
    #return result
    return float(hours)+ float_of_minutes

if __name__ == "__main__":
    main()