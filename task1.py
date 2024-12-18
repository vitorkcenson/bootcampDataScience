def password_validation():
    
    password = input("Enter your password: ")

    incorrect_attempts = []

    while True:
        confirm_password = input("Confirm your password: ")

        if confirm_password == password:
            print("Password confirmed!")
            print("Correct password: ", password)
            print("Incorrect attempts: ", incorrect_attempts)
            break
        else:
            incorrect_attempts.append(confirm_password)
            print("Incorrect password. Please try again.")

if __name__ == "__main__":
    password_validation()