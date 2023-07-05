def convert(n):
    if n >= 0:
        return convert_positive(n)
    else:
        return convert_negative(n)

def convert_positive(n):
    result = ""
    
    while n > 0:
        result = str(n % 2) + result
        n = n // 2

    while len(result) < 8:
        result = "0" + result

    return result

def convert_negative(n):
    positive_binary = convert_positive(-n)
    flipped_bits = ""
    for bit in positive_binary:
        if bit == "0":
            flipped_bits += "1"
        else:
            flipped_bits += "0"
    
    result = ""
    carry = 1
    for bit in flipped_bits[::-1]:
        if bit == "0" and carry == 1:
            result = "1" + result
            carry = 0
        elif bit == "1" and carry == 1:
            result = "0" + result
        else:
            result = bit + result
    
    return result

print(convert(56))
print(convert(-56))
