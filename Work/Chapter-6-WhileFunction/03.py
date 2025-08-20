def table(n,limit):
    n = 1
    while n <= limit:
        print((limit), "x" ,(n), "= ",(n * limit))
        n += 1 
n = int(input())
limit = int(input())
table(n, limit)
    