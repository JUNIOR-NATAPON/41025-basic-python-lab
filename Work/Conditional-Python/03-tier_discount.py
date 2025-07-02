price = int(input()) # Input the price of the product
if price >= 2000: # if the price greater than or equal to 2000
    total = price - (price * 0.15) # 15% discount
elif price >= 1000: # if the price is greater than or equal to 1000
    total = price - (price * 0.10) # 10% discount
elif price >= 500: # if the price is greater than or equal to 500
    total = price - (price * 0.05) # 5% discount
else:
    total = price # No discount