def convert(n):
    result = ""

    # Check if the number is negative
    is_negative = False
    if n < 0:
        is_negative = True
        n = abs(n)

    # Convert the absolute value to binary representation
    while n > 0:
        result = str(n % 2) + result
        n = n // 2

    # If the number is negative, invert all bits and add 1
    if is_negative:
        result = invert_bits(result)
        result = add_one(result)

    return result

def invert_bits(binary):
    inverted = ""
    for bit in binary:
        if bit == "0":
            inverted += "1"
        else:
            inverted += "0"
    return inverted

def add_one(binary):
    result = ""
    carry = 1
    for bit in binary[::-1]:  # Reverse the binary string
        if bit == "0" and carry == 1:
            result = "1" + result
            carry = 0
        elif bit == "1" and carry == 1:
            result = "0" + result
            carry = 1
        else:
            result = bit + result
    if carry == 1:
        result = "1" + result
    return result

print(convert(56))
