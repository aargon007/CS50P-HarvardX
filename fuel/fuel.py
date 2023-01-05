while True:
    fuel = input("Fraction: ")
    try:
        x,y = fuel.split("/")
        fuel_per=int(x)/int(y)
        if fuel_per <= 1 :
            break
    except(ValueError, ZeroDivisionError):
        pass
#totall  fuel percentage
fuel_in_tank= round(fuel_per * 100)

if fuel_in_tank <= 1:
    print("E")
elif fuel_in_tank >=99:
    print("F")
else:
    print(f"{fuel_in_tank}%")