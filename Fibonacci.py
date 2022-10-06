def fib(num):
    num1, num2 = 0, 1
    num0 = 0
    while num0 < num:
        print(num1, end=' , ')
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        num0 += 1


n = int(input("Enter the number:  "))
print(fib(n))
