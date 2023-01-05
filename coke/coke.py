#coke price
amount_due = 50

#insert coin until amount due is paid
while amount_due > 0:
    #print amount due
    print("Amount Due: ", amount_due)
    #prompts the user to insert a coin
    coin = int(input("Insert Coin: "))
    #check coin
    if coin in [25,10,5]:
        #subtract value from amount_due
        amount_due -= coin

#change owed
change_owed = abs(amount_due)
#print the result
print("Change Owed: " , change_owed)