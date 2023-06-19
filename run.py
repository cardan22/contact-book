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
    If the user wants to add a new contact, it calls the add_contact() function.
    """
    while True:
        print("\nWelcome to Contact Book!\n")
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. Display all contacts")
        print("4. Delete a contact")
        print("5. Exit\n")

        data_str = input (Fore.CYAN + "Please enter your choice (1-5 and press enter): \n" + Style.RESET_ALL)

        try:
            value = int(data_str)
            if not (1 <= value <= 5):
                raise ValueError(Fore.RED + f"\nInvalid value: {value} Please enter a number from 1 to 5.")
        except ValueError as e:
            print(Fore.RED + f"\n{e} Please try again.\n" + Style.RESET_ALL)
            continue

        if value == 1:
            add_contact()
        else: 
            print("\nThe function is not implemented yet.")        
       

def validate_input(prompt, data_type):
    """
    "This function validates user input based on the specified data type 
    and returns the validated input value. It takes two arguments:
    prompt (str): The message to display as a prompt.
    data_type (str): The type of data to validate. Supported values are 'name', 'email', and 'phone'.
    The function returns a string, which is the validated input value. 
    If the input value does not match the specified data type, a ValueError is raised."
    """  
    while True:
        value = input(prompt)

        if data_type == "name":
            if not value.replace(" ", "").isalpha():
                print(Fore.RED + "\nInvalid name: Only letters and blank spaces are allowed.\n" + Style.RESET_ALL)
                continue
        elif data_type == "email":
            if "@" not in value:
                print(Fore.RED + "\nInvalid email: Must contain the @ symbol.\n" + Style.RESET_ALL)
                continue
        elif data_type == "phone":
            if not value.replace(" ", "").isdigit():
                print(Fore.RED + "\nInvalid phone: Only numbers are allowed, and no blank spaces.\n" + Style.RESET_ALL)
                continue
        else:
            print(Fore.RED + "\nInvalid data type.\n" + Style.RESET_ALL)
            continue

        return value                                  

def add_contact():
    """
    Allows the user to enter contact details (name, email, and phone), 
    validates the input, and adds the contact to the Google Sheet if confirmed by the user.

    This function prompts the user to enter contact details and validates each input.
    If the input is valid, it displays the entered details and asks for confirmation 
    to add the contact. If the user confirms, the contact is added to the Google Sheet.
    After adding the contact, the function provides options to return to the start or exit the program.
    """
    while True:
        name = validate_input("Enter contact name: ", "name")
        email = validate_input("Enter contact email: ", "email")
        phone = validate_input("Enter contact phone: ", "phone")

        new_contact = {'Name': name, 'Email': email, 'Phone': phone}
        contact_worksheet = SHEET.worksheet("contact")

        print("\nContact details:")
        print("-------------------------")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print("-------------------------")

        while True:
            choice = input(Fore.CYAN +"\nDo you want to add the contact? ('Y' for yes or 'N' for no):\n" + Style.RESET_ALL)

            if choice.upper() == "Y":
                contact_worksheet.append_row(list(new_contact.values()))
                print(Fore.GREEN + "\nContact added successfully!\n" + Style.RESET_ALL)
            elif choice.upper() == "N":
                print("\nThe contact has not been added to the Contact Book.\n") 
            else:
                print(Fore.RED +"\nInvalid choice. Please try again." + Style.RESET_ALL)
                continue
            
            while True:
                exit_choice = input(Fore.CYAN + "Press 'S' to go to start or 'E' to exit: \n" + Style.RESET_ALL)
                
                if exit_choice.upper() == "S":
                    print("\nStarting from the beginning.\n")
                    display_contact_menu() 
                elif exit_choice.upper() == "E":
                    print("\nGoodbye, I hope to see you soon!\n")
                    exit()
                else:
                    print(Fore.RED + "\nInvalid choice. Please try again.\n" + Style.RESET_ALL)        

        
display_contact_menu() 