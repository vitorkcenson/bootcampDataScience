def register_students():
  """
  This function registers students by prompting the user for the number of students 
  and then collecting their student IDs. 

  The student IDs are appended to a file named "reg_form.txt". 
  Each student ID is written on a separate line followed by a separator.

  Args:
    None

  Returns:
    None
  """
  try:
    num_students = int(input("How many students are registering? "))  # Get the number of students to register
  except ValueError:
    print("Invalid input. Please enter a valid number.")
    return # Exit the function if an invalid input is provided

  with open("reg_form.txt", "a") as file:  # Open the file in append mode ('a') to add data without overwriting existing content
    for _ in range(num_students):
      student_id = input("Enter student ID number please: ")  # Get the student ID from the user

      file.write(student_id + "\n")  # Write the student ID to the file followed by a newline character
      file.write(".......................\n")  # Write a separator line to the file

  print("Thanks! Student registration complete!")  # Print a success message to the user

# Run the registration function
register_students()