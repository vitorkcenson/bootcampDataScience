def password_validation():
    """
    This function prompts the user for a password and validates it with a confirmation. 
    It keeps track of incorrect attempts and provides feedback to the user.
    """

    password = input("Enter your password: ")  # Get the initial password from the user

    incorrect_attempts = []  # Create an empty list to store incorrect attempts

    while True:  # Loop continuously until the correct password is entered
        confirm_password = input("Confirm your password: ")  # Get the confirmation from the user

        if confirm_password == password:  # Check if the password and confirmation match
            print("Password confirmed!")
            print("Correct password:", password)
            print("Incorrect attempts:", incorrect_attempts)
            break  # Exit the loop since the password is correct

        else:  # If the passwords don't match
            incorrect_attempts.append(confirm_password)  # Store the incorrect attempt
            print("Incorrect password. Please try again.") 

if __name__ == "__main__":
    password_validation()  # Call the function to start the password validation process