# Initialize variables to store the sum of valid numbers and their count
numberSum = 0 
numberCount = 0

# Continuously prompt the user for input until -1 is entered
while True:
    number = int(input("Please enter integers numbers to calculate the average: "))

    # Check if the user wants to quit by entering -1
    if number == -1:
        # Print a message if no valid numbers were entered
        print("Not valid! Stopping code!")
        break 

    # Check if the entered number is valid (not zero)
    if number != 0:
        # If valid, add the number to the sum and increment the count
        numberSum += number 
        numberCount += 1 
    else:
        # Print an error message if zero is entered
        print("0 is not a valid number to input!")

# Calculate and print the average if at least one valid number was entered
if numberCount > 0: 
    average = numberSum / numberCount 
    print("The average of the valid numbers is: ", round(average, 2)) 