def abc():
    array = []  
    while True:
        n = input()
        if n == "end":
            break
        array.append(int(n))
    print(max(array))
    print(min(array))
abc()


