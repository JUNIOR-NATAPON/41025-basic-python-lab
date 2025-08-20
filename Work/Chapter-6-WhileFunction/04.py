def function(n):
    if n <= 0 and n >= 20:
        return "Invalid input"
    i = 1
    while i <= n:
        n *= i
        i += 1 
    print(n)
n = int(input())
function(n)