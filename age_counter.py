try:
    user_input = input("Please enter your age: ")
    
    age = int(user_input)
    
    if age % 2 == 0:
        print(f"The age {age} is Even.")
    else:
        print(f"The age {age} is Odd.")

except ValueError:
    print("Value Error: Please enter a valid whole number for age.")
