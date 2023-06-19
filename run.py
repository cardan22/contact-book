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
    print("\nWelcome to Contact Book!\n")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Display all contacts")
    print("4. Delete a contact")
    print("5. Exit\n")

    data_str = input ("Please enter your choice (1-5 and press enter): \n")

display_contact_menu()    