import gspread
from google.oauth2.service_account import Credentials

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
    Displays a welcome message and the menu for the Contact Book.
    """
    while True:
        print("\nWelcome to Contact Book!\n")
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. Display all contacts")
        print("4. Delete a contact")
        print("5. Exit\n")

        data_str = input ("Please enter your choice (1-5 and press enter): \n")

        try:
            value = int(data_str)
            if not (1 <= value <= 5):
                raise ValueError(f"\nInvalid value: {value}, Please enter a number from 1 to 5.")
        except ValueError as e:
            print(f"\n{e} Please try again.\n")
            continue

        if value == 1:
            add_contact()
        else: 
            print("The function is not implemented yet.")        
       

def validate_input(prompt, data_type):
    """
    Validates the user input based on the specified data type.
    Returns the validated input value.
    """  
    while True:
        value = input(prompt)

        if data_type == "name":
            if not value.replace(" ", "").isalpha():
                print("\nInvalid name: Only letters and blank spaces are allowed.\n")
                continue
        elif data_type == "email":
            if "@" not in value:
                print("\nInvalid email: Must contain the @ symbol.\n")
                continue
        elif data_type == "phone":
            if not value.replace(" ", "").isdigit():
                print("\nInvalid phone: Only numbers are allowed, and no blank spaces.\n")
                continue
        else:
            print("\nInvalid data type.\n")
            continue

        return value                                  

def add_contact():
    """
    A function that lets the user enter contact details as (name, email, and phone),
    validates the input, and adds the contact to the Google Sheet if confirmed by the user.
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

        contact_worksheet.append_row(list(new_contact.values()))
        print("\nContact added successfully!\n")
        return


display_contact_menu()    