def convert_to_binary(decimal_number):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % 2
        remainder_stack.append(remainder)
        decimal_number = decimal_number // 2

    binary_digits = []
    while remainder_stack:
        binary_digits.append(str(remainder_stack.pop()))
    
    return ''.join(binary_digits)

print(convert_to_binary(42)) # '101010'