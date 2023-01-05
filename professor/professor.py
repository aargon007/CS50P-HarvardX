import sys

import random

def main():
    #call
    level = get_level()
    #get score
    score = simulate_p(level)
    #print
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    #get random integer
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

#simulate round
def simulate_round(x,y):
    count_try = 1
    while count_try <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                print("EEE")
                count_try +=1
        except:
            print("EEE")
            count_try +=1


    print(f"{x} + {y} = {x+y}")
    return False
#simulate
def simulate_p(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        response = simulate_round(x,y)
        if response == True:
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()