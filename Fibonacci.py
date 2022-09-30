def fib(num):
    n1, n2 = 0, 1
    n0 = 0
    while n0 < num:
        print(n1, end=' , ')
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n0 += 1


n = int(input("Enter the number:  "))
print(fib(n))
