#get user input
greet=input("Greeting: ")
#lowercase and remove whitespace
greet=greet.lower().strip()
#if say hello pay nothing
if "hello" in greet:
    print("$0")

#if say h+ pay $20
elif "h"==greet[0]:
    print("$20")

#else pay $100
else:
    print("$100")