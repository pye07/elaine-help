payment = float(input("Coffee costs $3.50. How much cash will you give? $"))
if payment < float(3.5):
    print("Insufficient funds.")
elif payment == float(3.5):
    print ("Your drink will be out soon. Thank you!")
elif payment > float(3.5):
    change = float(payment - 3.5)
    print ("Your change is $", change, ". Your drink will be out soon. Thank you!")