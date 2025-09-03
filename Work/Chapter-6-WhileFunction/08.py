import random
def g(n):
    t = 0
    i = 0
    while True:
        i = int(input())
        if i > n:
            print("มากไป")
            t += 1
        elif i < n:
            print("น้อยไป")
            t += 1
        else:
            print("ถูกต้องจำนวนครั้งที่ทาย:", t)
            break   
g(random.randint(1, 20))