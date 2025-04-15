# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = "Medium"
extra_short = True

if extra_short:
    coffee = order_size + " Coffe with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)