times = int(input())
num = []
for i in range(times):
    n = int(input())
    if n > 50:
        num.append(n)
print("จำนวนที่มากกว่า 50: ",len(num))