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

        if validate_data(data_str):
            continue

def validate_data(data_str):
    """
    Validates user input to ensure it is an integer between 1 and 5.
    Raises a ValueError if the input is invalid.
    """
    try:
        value = int(data_str)
        if not (1 <= value <= 5):
            raise ValueError(f"\nInvalid value: {value}, Please enter a number from 1 to 5.")
    except ValueError as e:
        print(f"\n{e} Please try again.\n")
        return False

    return True            

def add_contact():
    """
    A function that lets the user enter contact details as (name, email, and phone),
    validates the input, and adds the contact to the Google Sheet if confirmed by the user.
    """
    name = input("Enter contact name: ")
    email = input("Enter contact email: ")
    phone = input("Enter contact phone: ")

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


add_contact()    