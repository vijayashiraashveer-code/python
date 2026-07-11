def shutdown(user_input):
    user_input = user_input.lower()
    
    if user_input == "yes":
        print("shutting down")
    elif user_input == "no":
        print("abort shut down")
    else:
        print("sorry")

# Taking input from the user
status = input("Do you want to shut down? (Yes/No): ")
shutdown(status)