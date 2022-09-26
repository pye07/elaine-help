payment = float(input("Coffee costs $3.50. How much cash will you give? $"))
price = float(3.50)
if payment < price:
    print("Insufficient funds.")
elif payment == price:
    print ("Your drink will be out soon. Thank you!")
elif payment > price:
    change = float(payment - 3.5)
    print ("Your change is $", change, ". Your drink will be out soon. Thank you!")