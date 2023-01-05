x=input("What is the answer to the Great Question of Life, the Universe, and Everything?")

if x.strip() == "42":
    print("Yes")

elif x == "forty-two":
    print("Yes")

elif x == "forty two":
    print("Yes")

elif x == "Forty Two":
    print("Yes")
elif x == "FoRty TwO":
    print("Yes")
else:
    print("No")