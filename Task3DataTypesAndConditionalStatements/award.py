# These lines prompt the user to enter their swimming, cycling, and running times in minutes.
# Get user input for swimming time
swimming_time = float(input("Enter your swimming time (minutes): ")) 
# Get user input for cycling time
cycling_time = float(input("Enter your cycling time (minutes): ")) 
# Get user input for running time
running_time = float(input("Enter your running time (minutes): "))

# The float() function converts the user's input (which is initially a string) to a floating-point number, allowing for times with decimal values

# Calculate the total time
total_time = (swimming_time + cycling_time + running_time) 
# Print the total time
print("The total time in minutes was ", total_time)

# Determine and print the award based on total time
if total_time < 100 :
    print("Award: Honorary colours.")
elif total_time >= 101 and total_time <= 105 :
    print("Award: Honorary half colours.")
elif total_time >= 106 and total_time <= 110 :
    print("Award: Honorary scroll")
else : total_time >= 111 
print("No award.")