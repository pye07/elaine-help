drink = str(input("What drink would you like?"+"\n1. Espresso (Small $1.75, Medium $3.50, Large $5.25)"+"\n2. Americano (Small $1.75, Medium $3.50, Large 5.25)"+"\n3. Latte (Small $1.75, Medium $3.50, Large 5.25)"+"\n4. Cappuccino (Small $1.75, Medium $3.50, Large 5.25)\n\n"))
if drink == "1":
    cost = float(1.75)
    print("You ordered an espresso.")
elif drink == "2":
    cost = float(1.75)
    print("You ordered an americano.")
elif drink == "3":
    cost = float(1.75)
    print("You ordered a latte.")
elif drink == "4":
    cost = float(1.75)
    print("You ordered a cappuccino.")
else:
    print("Error. Invalid drink option.")
    
size = input("\nWhat size drink would you like? Small (S), medium (M), or large (L)? \n\n").lower()
price = float(3.5)
if size == "s":
    multiplier = int(1)
    print("You ordered a small drink.")
elif size == "m":
    multiplier = int(2)
    print("You ordered a medium drink.")
elif size == "l":
    multiplier = int(3)
    print("You ordered a large drink.")
else:
    print("Error. Invalid drink size.")
    
price = float(cost * multiplier)

payment = float(input("\nYour drink will be $" + str(price) + ". How much cash will you give? \n\n$"))
if payment < price:
    print("Insufficient funds.")
elif payment == price:
    print ("Your drink will be out soon. Thank you!")
elif payment > price:
    change = float(payment - price)
    print ("Your change is $",change, ". Your drink will be out soon. Thank you!")
