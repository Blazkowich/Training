def decimal_to_hexadecimal(number):
    result = ""
    while number > 0:
        remainder = number % 16
        result = str(remainder) +" " + result
        number = number // 16
    return result

decimal_number = 45891
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print(hexadecimal_number)

def hexadecimal_to_decimal(hexadecimal_number):
    decimal = 0
    power = 0
    for digit in reversed(hexadecimal_number):
        if digit.isdigit():
            decimal += int(digit) * (16 ** power)
        else:
            decimal += (ord(digit.upper()) - 55) * (16 ** power)
        power += 1
    return decimal

hexadecimal_number = "B43"
decimal_number = hexadecimal_to_decimal(hexadecimal_number)
print(decimal_number)

