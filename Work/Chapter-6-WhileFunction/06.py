def add(a, b):return a + b
def sub(a, b):return a - b
def mul(a, b):return a * b
while True:
    c = int(input())
    if c == 4:break
    a = int(input())
    b = int(input())
    if c == 1:print(add(a, b))
    elif c == 2:print(sub(a, b))
    elif c == 3:print(mul(a, b))
    else:print("Invalid input")
