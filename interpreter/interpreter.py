#get user input
expression = input("Expression: ")
#convert this into variable
x, y, z = expression.split(" ")
#change type of variable x and z to float
new_x=float(x)
new_z=float(z)
#calculate the result
if y == "+":
    result = new_x + new_z

elif y == "-":
    result = new_x - new_z

elif y == "*":
    result = new_x * new_z

elif y == "/":
    result= new_x / new_z

print(round(result,1))