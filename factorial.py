number = int(input("Enter the number : "))
startNum = 1

for num in range(1, number + 1):
    startNum = startNum * num
print("The Factorial of %d = %d" % (number, startNum))
