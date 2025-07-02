day =int(input())
if day >=1 and day <= 5: # Check if the day is between 1 and 5
    print("Weekday")
elif day == 6 or day == 7: # Check if the day is 6 or 7
    print("Weekend")