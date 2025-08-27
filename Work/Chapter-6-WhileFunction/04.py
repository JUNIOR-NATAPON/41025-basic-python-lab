def function(n):
    if n <= 0 and n >= 20:
        return "Invalid input"
    sum = 1
    i = 1
    while i <= n:
        sum *= i
        i += 1 
    return sum
n = int(input())
print(function(n))