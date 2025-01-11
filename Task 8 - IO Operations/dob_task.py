def read_and_print_data(filename):
    """
    Reads data from the specified file, extracts names and birthdates,
    and prints them in separate sections.

    Args:
        filename: The name of the file to read.
    """

    try:
        with open("DOB.txt", 'r') as file:
            lines = file.readlines()

        names = []
        birthdates = []

        for line in lines:
            parts = line.strip().split()  # Split each line into a list of words
            if len(parts) >= 3:  # Ensure there are at least 3 parts (name and birthdate)
                name = ' '.join(parts[:-3])  # Combine first and middle names
                birthdate = ' '.join(parts[-3:])
                names.append(name)
                birthdates.append(birthdate)

        print("Name")
        for name in names:
            print(name)

        print("\nBirthdate")
        for birthdate in birthdates:
            print(birthdate)

    except FileNotFoundError:
        print(f"Error: File '{"DOB.txt"}' not found.")

# Example usage:
read_and_print_data("DOB.txt")