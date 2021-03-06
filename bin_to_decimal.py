def bin_to_decimal(binary_number):
    ''' Converts a binary number to decimal '''
    binary_number = str(binary_number)
    bytes = []
    bit = 1
    for _ in binary_number:  # Sets the array of bytes
        bytes.append(bit)
        bit *= 2
    bytes.reverse()
    decimal_number = 0
    for b in range(len(binary_number)):
        if binary_number[b] == "1":
            decimal_number += bytes[b]
    return decimal_number
