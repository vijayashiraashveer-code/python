
user_input = input("Enter a single character: ")


if type(user_input) is str and len(user_input) == 1:
    
    
    ascii_value = ord(user_input)
    print(f"The ASCII value of '{user_input}' is: {ascii_value}")

    if 65 <= ascii_value <= 90:
        print("Category: Uppercase Letter")
    elif 97 <= ascii_value <= 122:
        print("Category: Lowercase Letter")
    elif 48 <= ascii_value <= 57:
        print("Category: Digit")
    else:
        print("Category: Special Character")

else:
    print("Error: Please enter exactly one character.")