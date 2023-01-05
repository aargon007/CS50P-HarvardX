import random

#prompts the user for a level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

#set random number
random_number = random.randint(1, level)
#prompt guess and loop
while True:
    try:
        guess = int (input("Guess: "))
        if guess > 0:
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break

    except:
        pass