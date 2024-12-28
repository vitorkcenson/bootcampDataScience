arrowAscending = True  # Flag to indicate the current direction of the arrow (ascending initially)

stars = "*"  # Initialize the string with a single star

for i in range(9):  # Iterate 9 times (for 10 rows in the arrow)
    print(stars)  # Print the current row of stars

    if arrowAscending:  # If the arrow is currently ascending
        stars += "*"  # Add a star to the string
    else:  # If the arrow is descending
        stars = stars[:-1]  # Remove the last star from the string

    if i == 3:  # Change direction after the 4th row (index 3)
        arrowAscending = False