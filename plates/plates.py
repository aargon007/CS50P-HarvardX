def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #vanity pale contains max 6 and min 2 char
    if len(s) < 2 or len(s) > 6:
        return False
    #vanity plate start with at least 2 letter
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    #number cant be at middle
    i=0
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
            else:
                break
    #number must be at the end, first number can't 0
    while i< len(s):
        if s[i].isalpha() == False:
            if s[i] =="0":
                return False
            else:
                break
        i += 1

    #no periods, space, or punctuation marks are allowed
    for c in s:
        if c in [".", " ", "!", "?"]:
            return False

#print if all are true
    return True

main()