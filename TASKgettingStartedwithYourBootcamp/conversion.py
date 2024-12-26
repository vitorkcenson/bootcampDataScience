# Define variables with different data types
num1 = 99.23  # Float. Defines a variable num1 and assigns it the floating-point value 99.23.
num2 = 23     # Integer. Defines a variable num2 and assigns it the integer value 23.
num3 = 150    # Integer. Defines a variable num3 and assigns it the integer value 150.
string1 = "100"  # String. Defines a variable string1 and assigns it the string value "100".

# Convert num1 (float) to an integer (will truncate the decimal part)
newnum1 = int(num1) 
# Converts the float value num1 to an integer. Since int() truncates the decimal part, newnum1 will be 99.

# Convert num2 (integer) to a float (no change in value, but now a float)
newnum2 = float(num2) 
#Converts the integer value num2 to a float. This doesn't change the value, but now it's represented as a floating-point number.

# Convert num3 (integer) to a string
newnum3 = str(num3) 
# Converts the integer value num3 to a string. This will result in the string "150".

# Convert string1 (string representing an integer) to an integer
newstring1 = int(string1) 
# Converts the string value string1 (which represents an integer) to an integer. This is valid because the string contains only digits.

# Print the results of the type conversions
print("The new number 1 is: {}.".format(newnum1))
print("The new number 2 is: {}.".format(newnum2))
print("The new number 3 is: {}.".format(newnum3))
print("The new string 1 is: {}.".format(newstring1)) 