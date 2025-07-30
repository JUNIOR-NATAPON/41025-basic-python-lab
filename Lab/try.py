num = int(input("How many numbers? "))
total = []
for i in range(num):
    total.append(int(input("Enter number: ")))
print(total)
total.sort()
print(total)