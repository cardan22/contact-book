import gspread
from google.oauth2.service_account import Credentials
from colorama import init, Fore, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('contact_book')


def display_contact_menu():
    """
    Displays the Contact Book menu and handles the selected option.
    This function asks the user to choose an option from the menu.
    If the user wants to add a new contact,
    it calls the add_contact() function.
    """
    while True:
        print("\nWelcome to Contact Book!\n")
        print(Fore.CYAN + "1. " + Style.RESET_ALL + "Add a new contact")
        print(Fore.CYAN + "2. " + Style.RESET_ALL + "Search for a contact")
        print(Fore.CYAN + "3. " + Style.RESET_ALL + "Display all contacts")
        print(Fore.CYAN + "4. " + Style.RESET_ALL + "Delete a contact")
        print(Fore.CYAN + "5. " + Style.RESET_ALL + "Exit\n")

        data_str = input(
            Fore.CYAN +
            "Please enter your choice (1-5 and press enter): \n"
            + Style.RESET_ALL
            )

        try:
            value = int(data_str)
            if not (1 <= value <= 5):
                raise ValueError(
                    Fore.RED + f"\nInvalid value:" +
                    "{value} Please enter a number from 1 to 5."
                    )
        except ValueError as e:
            print(Fore.RED + f"\n{e} Please try again.\n" + Style.RESET_ALL)
            continue

        if value == 1:
            add_contact()
        elif value == 2:
            search_contact()
        elif value == 3:
            display_all_contacts()
        elif value == 4:
            delete_contact()
        elif value == 5:
            exit_contact_menu()
        else:
            print("\nPlease try again.")


def validate_input(prompt, data_type):
    """
    This function validates user input based on the specified data type
    and returns the validated input value. It takes two arguments:
    prompt (str): The message to display as a prompt.
    data_type (str): The type of data to validate. Supported values are
    'name', 'email', and 'phone'.
    The function returns a string, which is the validated input value.
    If the input value does not match the specified data type,
    a ValueError is raised."
    """
    while True:
        value = input(prompt)

        if data_type == "name":
            if not value.replace(" ", "").isalpha():
                print(
                    Fore.RED +
                    "\nInvalid name:" +
                    "Only letters and blank spaces are allowed.\n"
                    + Style.RESET_ALL
                    )
                continue
        elif data_type == "email":
            if "@" not in value:
                print(
                    Fore.RED +
                    "\nInvalid email: Must contain the @ symbol.\n" +
                    Style.RESET_ALL
                    )
                continue
        elif data_type == "phone":
            if not value.replace(" ", "").isdigit():
                print(
                    Fore.RED +
                    "\nInvalid phone:" +
                    "Only numbers are allowed, and no blank spaces.\n"
                    + Style.RESET_ALL
                    )
                continue
        else:
            print(Fore.RED + "\nInvalid data type.\n" + Style.RESET_ALL)
            continue

        return value


def add_contact():
    """
    Allows the user to enter contact details (name, email, and phone),
    validates the input, and adds the contact to the Google Sheet
    if confirmed by the user.

    This function prompts the user to enter contact details and
    validates each input. If the input is valid, it displays the entered
    details and asks for confirmation to add the contact. If the user confirms,
    the contact is added to the Google Sheet.
    After adding the contact, the function provides options to return
    to the start or exit the program.
    """
    while True:
        name = validate_input("Enter contact name:\n", "name")
        email = validate_input("Enter contact email:\n", "email")
        phone = validate_input("Enter contact phone:\n", "phone")

        new_contact = {'Name': name, 'Email': email, 'Phone': phone}
        contact_worksheet = SHEET.worksheet("contact")

        print("\nContact details:")
        print("-------------------------")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print("-------------------------")

        while True:
            choice = input(
                Fore.CYAN +
                "\nDo you want to add the contact?" +
                "('Y' for yes or 'N' for no):\n"
                + Style.RESET_ALL
                )

            if choice.upper() == "Y":
                contact_worksheet.append_row(list(new_contact.values()))
                print(
                    Fore.GREEN +
                    "\nContact added successfully!\n" + Style.RESET_ALL
                    )
            elif choice.upper() == "N":
                print(
                    "\nThe contact has not been added to the Contact Book.\n"
                    )
            else:
                print(
                    Fore.RED +
                    "\nInvalid choice. Please try again." + Style.RESET_ALL
                    )
                continue

            exit_choice()


def search_contact():
    """
    Allows the user to search for a contact in the Google Sheet based
    on the provided name or email, displaying the matching contacts.

    This function prompts the user to enter a name or email of the contact
    they want to search for.It searches the contacts in the Google Sheet and
    creates a list of matching contacts, if any.
    After displaying the results, it offers the option to search again
    or return to the start menu.
    """
    while True:
        search_term = input(
            Fore.CYAN +
            "\nEnter name or email of the contact you want to search for:\n"
            + Style.RESET_ALL
            )
        contact_worksheet = SHEET.worksheet("contact")
        contacts = contact_worksheet.get_all_records()

        found_contacts = []
        for contact in contacts:
            try:
                name_match = search_term.lower() in contact["Name"].lower()
                email_match = search_term.lower() in contact["Email"].lower()

                if name_match or email_match:
                    found_contacts.append(contact)
            except AttributeError:
                continue

        if found_contacts:
            print("\nFound contacts:")
            print("-------------------------")
            for contact in found_contacts:
                print(f"Name: {contact['Name']}")
                print(f"Email: {contact['Email']}")
                print(f"Phone: {contact['Phone']}")
                print("-------------------------")
        else:
            print("\nNo contacts found.")

        exit_choice = input(
            Fore.CYAN +
            "\nSearch again? ('Y' for yes or 'N' for no)\n" + Style.RESET_ALL
            )
        if exit_choice.upper() == "Y":
            search_contact()
        elif exit_choice.upper() == "N":
            print("\nYou will return to start.")
            print("-------------------------")
            display_contact_menu()
        else:
            print(
                Fore.RED +
                "\nInvalid choice. Please try again." + Style.RESET_ALL
                )


def display_all_contacts():
    """
    Displays all the contacts stored in the Google Sheet.

    This function gets all the contact records from the Google Sheet
    and shows them in an organized way. If there are contacts available,
    it prints the name, email, and phone number of each contact.
    If no contacts are found, it prints a message saying that
    there are no contacts.

    After showing the contacts, the function gives options to go back
    to the start or exit the program.
    """
    while True:
        contact_worksheet = SHEET.worksheet("contact")
        contacts = contact_worksheet.get_all_records()

        if contacts:
            print("\nA list of all contacts:")
            print("-------------------------")
            for contact in contacts:
                print(f"Name: {contact['Name']}")
                print(f"Email: {contact['Email']}")
                print(f"Phone: {contact['Phone']}")
                print("-------------------------")
        else:
            print("\nNo contacts found.")

        exit_choice()


def delete_contact():
    """
    Allows the user to delete a contact from the contact book.

    The function prompts the user to enter the name or email of
    the contact they want to delete. It searches for contacts that match
    the search term and displays the matching contacts. The user is then asked
    to choose the contact they want to delete by entering
    the corresponding number. The chosen contact is displayed,
    and the user is asked to confirm the deletion.
    If confirmed, the contact is deleted from the contact book.

    After deleting a contact, the user can choose to search for another contact
    to delete or return to the main menu.
    """
    while True:
        search_term = input(
            Fore.CYAN +
            "\nEnter the name or email of the contact you want to delete:\n" +
            Style.RESET_ALL
            )
        contact_worksheet = SHEET.worksheet("contact")
        contacts = contact_worksheet.get_all_records()

        found_contacts = []
        for contact in contacts:
            try:
                name_match = search_term.lower() in contact["Name"].lower()
                email_match = search_term.lower() in contact["Email"].lower()

                if name_match or email_match:
                    found_contacts.append(contact)
            except AttributeError:
                continue

        if found_contacts:
            print("\nFound contacts:")
            print("-------------------------")
            for index, contact in enumerate(found_contacts):
                print(f"{index + 1}. Name: {contact['Name']}")
                print(f"Email: {contact['Email']}")
                print(f"Phone: {contact['Phone']}")
                print("-------------------------")
        else:
            print("\nNo contacts found.")
            continue

        while True:
            delete_choice = input(
                Fore.CYAN +
                "\nEnter the number of the contact you want to delete" +
                "(or 'C' to cancel):\n"
                + Style.RESET_ALL
                )
            if delete_choice.upper() == "C":
                print("\nDeletion canceled. You will return to start.")
                print("-------------------------")
                display_contact_menu()
            else:
                try:
                    delete_index = int(delete_choice) - 1
                    if not (0 <= delete_index < len(found_contacts)):
                        raise ValueError()
                    break
                except ValueError:
                    print(
                        Fore.RED +
                        "\nInvalid choice. Please try again." +
                        Style.RESET_ALL
                        )

        contact_to_delete = found_contacts[delete_index]
        print("\nContact details:")
        print("-------------------------")
        print(f"Name: {contact_to_delete['Name']}")
        print(f"Email: {contact_to_delete['Email']}")
        print(f"Phone: {contact_to_delete['Phone']}")
        print("-------------------------")

        while True:
            confirm_choice = input(
                Fore.CYAN +
                "\nAre you sure you want to delete this contact?" +
                "('Y' for yes or 'N' for no):\n" +
                Style.RESET_ALL
                )
            if confirm_choice.upper() == "Y":
                contact_worksheet.delete_rows(delete_index + 2)
                print(
                    Fore.GREEN +
                    "\nContact deleted successfully!" + Style.RESET_ALL
                    )
            elif confirm_choice.upper() == "N":
                print("\nContact deletion canceled.")
            else:
                print(
                    Fore.RED +
                    "\nInvalid choice. Please try again.\n" + Style.RESET_ALL
                    )
                continue

            while True:
                exit_choice = input(
                    Fore.CYAN +
                    "\nDo you want to search for another contact to delete?" +
                    "('Y' for yes or 'N' for no):\n" +
                    Style.RESET_ALL
                    )
                if exit_choice.upper() == "Y":
                    delete_contact()
                elif exit_choice.upper() == "N":
                    print("\nYou will return to start.")
                    print("-------------------------")
                    display_contact_menu()
                else:
                    print(
                        Fore.RED +
                        "\nInvalid choice. Please try again." + Style.RESET_ALL
                        )


def exit_choice():
    """
    Handles the choice to either return to the start menu or exit the program.

    This function let the user to choose between returning to the start menu
    or exiting the program. If the user chooses to return to the start menu,
    it calls the display_contact_menu() function. If the user chooses to exit
    the program, it displays a goodbye message and exits.
    """
    while True:
        choice = input(
            Fore.CYAN +
            "\nPress 'S' to go to start or 'E' to exit:\n" + Style.RESET_ALL
            )

        if choice.upper() == "S":
            print("\nYou will return to start.\n")
            print("-------------------------")
            display_contact_menu()
        elif choice.upper() == "E":
            exit_contact_menu()
        else:
            print(
                Fore.RED +
                "\nInvalid choice. Please try again." + Style.RESET_ALL
                )


def exit_contact_menu():
    """
    Displays an exit message and exits the program.
    """
    print("\nThank you for using Contact Book. Have a great day!\n")
    exit()


display_contact_menu()
