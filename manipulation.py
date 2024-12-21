# Get input from the user
str_manip = input("Enter a sentence: ")

# Calculate and print the length of the input string
str_manip_length = len(str_manip) 
print("The length of the string is: ", str_manip_length)

# Find and replace the last letter
last_letter = str_manip[-1]  # Get the last character
new_string = str_manip.replace(last_letter, "@")  # Replace the last letter with '@'
# Replaces all occurrences of the last_letter with the character @ using the replace() method.
print("String update: ", new_string)

# Reverse the last three letters
last_three_letters = str_manip[-3:]  # Get the last three characters
backwards_last_three_letters = last_three_letters[::-1]  # Reverse the order of the last three characters
print("The last three letters backwards is: ", backwards_last_three_letters)

# Create a new word from first three and last two letters
first_three_letters = str_manip[:3]  # Get the first three characters
last_two_letters = str_manip[-2:]  # Get the last two characters
print("The word with 5 letters is: ", first_three_letters + last_two_letters)