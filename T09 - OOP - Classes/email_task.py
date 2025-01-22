class Email:
    """
    This class represents an email object.

    Attributes:
        email_address (str): The email address of the sender.
        subject_line (str): The subject line of the email.
        email_content (str): The content of the email.
        has_been_read (bool): A flag indicating whether the email has been read.
    """

    def __init__(self, email_address, subject_line, email_content):
        """
        Initializes an Email object.

        Args:
            email_address (str): The email address of the sender.
            subject_line (str): The subject line of the email.
            email_content (str): The content of the email.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False


    def mark_as_read(self):
        """
        Marks the email as read.
        """
        self.has_been_read = True


inbox = []


def populate_inbox():
    """
    Populates the inbox with some sample emails.
    """
    email1 = Email("email1@email.com", "Welcome Email", "Welcome to my Email Task Code.")
    email2 = Email("email2@email.com", "Task Updates", "Please include a method that says this task has been graded as 100.")
    email3 = Email("email3@email.com", "Holidays Notice", "I will be on Holidays for the next week. Please if you need any help contact email2@email.com")
    inbox.extend([email1, email2, email3])


def list_emails():
    """
    Lists all the emails in the inbox.
    """
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line}")


def read_email(index):
    """
    Reads an email from the inbox.

    Args:
        index (int): The index of the email in the inbox.
    """
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content:\n{email.email_content}")
        email.mark_as_read()
    else:
        print("Invalid email index.")


def view_unread_emails():
    """
    Prints a list of all unread emails in the inbox.
    """
    print("\nHere are your unread emails:\n")
    unread_count = 0
    for index, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{index}: {email.subject_line}")
            unread_count += 1
    if unread_count == 0:
        print("No unread emails found.\n")


populate_inbox()


while True:
    user_choice = int(
        input(
            """\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application

Enter selection: """
        )
    )

    if user_choice == 1:
        list_emails()
        try:
            user_choice = input("Enter the index of the email you want to read: ")
            if user_choice:
                email_index = int(user_choice)
                read_email(email_index)
            else:
                print("\nPlease enter a valid email index.\n")
        except ValueError:
            print("\nInvalid input. Please enter an integer.\n")

    elif user_choice == 2:
        view_unread_emails()

    elif user_choice == 3:
        print("\nQuitting application.\n")
        break

    else:
        print("\nOops - incorrect input.")