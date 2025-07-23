num = int(input(""))
sum = 0
for i in range(num):
    if (i + 1) % 2 == 1:
        sum += i + 1
print(sum)