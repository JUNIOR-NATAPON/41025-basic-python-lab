times = int(input())
num = []
for i in range(times):
    n = int(input())
    if 10 < n < 50:
        num.append(n)
print("ค่าที่อยู่ในช่วง 10-50: ", num)