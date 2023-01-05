def main():
    dollars=dollars_to_float(input("How much was the meal? "))
    percent=percent_to_float(input("What percentage would you like to tip? "))
    #calculate tip
    tip = dollars * percent
    #print the output
    print(f"Leave ${tip:.2f}")

#define dollars_to_floatfunction
def dollars_to_float(d):
    dollars=d.replace("$"," ").strip()
    return float(dollars)
#define percent_to_float function
def percent_to_float(p):
    percent=p.replace("%"," ").strip()
    y=float(percent)/100
    return y

main()