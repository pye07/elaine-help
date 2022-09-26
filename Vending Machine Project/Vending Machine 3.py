drink = str(input("What drink would you like?"+"\n1. Espresso (Small $1.75, Medium $3.50, Large $5.25)"+"\n2. Americano (Small $1.75, Medium $3.50, Large 5.25)"+"\n3. Latte (Small $1.75, Medium $3.50, Large 5.25)"+"\n4. Cappuccino (Small $1.75, Medium $3.50, Large 5.25)\n"))
if drink == "1":
    cost = float(1.75)
    print("You ordered an espresso")
    print(cost)
elif drink == "2":
    cost = float(1.75)
    print("You ordered an americano")
    print(cost)
elif drink == "3":
    cost = float(1.75)
    print("You ordered a latte")
    print(cost)
elif drink == "4":
    cost = float(1.75)
    print("You ordered a cappuccino")
    print(cost)
else:
    print("Invalid drink option")