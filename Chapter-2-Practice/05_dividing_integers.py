egg = int(input()) # Input number of eggs
basket = egg // 30 # Calculate number of trays (30 eggs per tray)
egg_remainder = egg % 30 # Calculate remaining eggs after filling trays
print("Trays: " + str(basket) + " Remaining: " + str(egg_remainder)) # Output number of trays and remaining eggs