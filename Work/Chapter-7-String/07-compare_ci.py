a = input().strip()
b = input().strip()
a_lower = a.lower()
b_lower = b.lower()
if a_lower < b_lower:
    print("A comes before B")
elif a_lower > b_lower:
    print("A comes after B")
else:
    print("A equals B")