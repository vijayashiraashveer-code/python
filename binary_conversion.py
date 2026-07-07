# Program to convert decimal to binary
decimal_num = int(input("Enter a decimal number: "))

if decimal_num == 0:
    binary_result = "0"
else:
    binary_result = ""
    temp_num = decimal_num
    
    # Using a while loop as per project goals
    while temp_num > 0:
        remainder = temp_num % 2
        binary_result = str(remainder) + binary_result
        temp_num = temp_num // 2

print(f"The binary representation of {decimal_num} is: {binary_result}")