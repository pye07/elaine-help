size = input("What size drink would you like? Small (S), medium (M), or large (L)? ").lower()
price = float(3.5)
if size == "s":
    multiplier = int(1)
    print("You ordered a small drink.")
    print("Price multiplier: ", multiplier)
elif size == "m":
    multiplier = int(2)
    print("You ordered a medium drink.")
    print("Price multiplier: ", multiplier)
elif size == "l":
    multiplier = int(3)
    print("You ordered a large drink.")
    print("Price multiplier: ", multiplier)
else:
    print("Invalid drink size.")
