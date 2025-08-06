odd = []; even = []
num = int(input())
for i in range(num):
    n = int(input())
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print(even)
print(odd)