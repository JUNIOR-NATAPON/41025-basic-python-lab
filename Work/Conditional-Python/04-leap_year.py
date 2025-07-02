year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): #check if the year is a leap year
    print("Leap Year")   #print "Leap Year"
else:
    print("Not a Leap Year") #print "Not a Leap Year"