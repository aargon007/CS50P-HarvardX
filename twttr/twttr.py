#get the user input
input_text = input("Input: ")

#print the output
print("Output :", end="")
for letter in input_text:
    if not letter.lower() in ["a", "e", "i", "o", "u"]:
      print(letter, end="")
#print the line
print()