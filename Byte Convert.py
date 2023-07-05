def byte(number):
    result = ""
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result
print(byte(63425658))

def binary_to_decimal(binary_number):
    decimal = 0
    power = 0
    for digit in reversed(binary_number):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

binary_number = "11110011010101011001001010"
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)

