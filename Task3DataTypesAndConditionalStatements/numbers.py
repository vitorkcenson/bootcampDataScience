# Get input from the user.
# The int() function converts the user's input (which is initially a string) to an integer.
num1 = int(input("Enter an first integer number: ")) 
num2 = int(input("Enter an second integer number: ")) 
num3 = int(input("Enter an third integer number: "))

# Calculate and print the sum of the numbers
print("The sum of the numbers is: ", num1 + num2 + num3) 

# Calculate and print the difference between the first and second number
print("The first number minus the second number is: ", num1 - num2) 

# Calculate and print the product of the third and first number
print("The third number multiplied by the first number is: ", num3 * num1) 

# Calculate and print the sum of all numbers divided by the third number
print("The sum of all three numbers divided by the third number is: ", (num1 + num2 + num3) / num3) 