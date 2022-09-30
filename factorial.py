number = int(input("Enter the number : "))
factorial = 1

for num in range(1, number + 1):
    factorial *= num
    print("The Factorial of %d = %d" % (number, factorial))
