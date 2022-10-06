number = int(input("Enter the number : "))
startNumber = 1

for num in range(1, number + 1):
    startNumber = startNumber * num
print("The Factorial of %d = %d" % (number, startNumber))
