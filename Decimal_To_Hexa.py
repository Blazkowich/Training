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
