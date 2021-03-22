##
# list_functions.py
# 23/3/21

drinks = []

# .append adds to the end of the list
drinks.append("Ice Chocolate")
drinks.append("Fanta Frozen Grape")
drinks.append("Sprite")

# Print drinks
print(drinks)

drinks.insert(1, "Liquid Nitrogen")
drinks.insert(10, "Chloroform")
drinks.insert(8, "Pepsi")

print(drinks)

drinks.pop(4)
drinks.pop(1)

print(drinks)
