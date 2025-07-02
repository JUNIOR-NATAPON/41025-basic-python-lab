age = int(input())
days = int(input())
if age < 13: # Check if the age is less than 13
    ticket_price = 100
elif age < 60: # Check if the age is between 13 and 59
    ticket_price = 180
elif age >= 60: # Check if the age is 60 or older
    ticket_price = 120
if days == 6 or days == 7: # Check if the day is Saturday or Sunday
    ticket_price += 50
print(ticket_price)