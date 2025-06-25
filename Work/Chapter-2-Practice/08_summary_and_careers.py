price = float(input()) # Input price of the meal
tip = price + (price * 0.15) # Calculate total price with 15% tip
customer = int(input()) # Input number of customers
total = tip / customer # Calculate each person's share of the total price
print("Each person pays: " + str(round(total, 2))) # Output each person's share rounded to 2 decimal places 
