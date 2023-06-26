# Contact Book

Link to the project: [Contact Book](https://contact--book-ebd067fbca38.herokuapp.com/)

# About
The Contact Book is a Python application that simplifies contact management for users. Whether it's personal or professional contacts, this application enables users to effortlessly add, search, display, and delete contact information. By using Google Sheets as the backend storage, users can access their contacts from anywhere and ensure secure cloud-based storage.

# UX

## User Demographic
The Contact Book aims to provide a user-friendly experience with a simple and intuitive interface. The menu-driven design ensures easy navigation through different features and actions. Clear instructions and input validation help users enter accurate contact details. The integration with Google Sheets ensures seamless data storage and retrieval, enhancing the overall user experience.

## User stories
* As a user, I want to easily add new contacts to my contact list, including their name, email, and phone number.
* As a user, I want to be able to search for specific contacts by their name or email address.
* As a user, I want to view all my contacts in a well-organized manner, displaying their names, email addresses, and phone numbers.
* As a user, I want the option to delete a contact from my contact list if it is no longer relevant.

## User goals

* Easily add new contacts with accurate details.
* Quickly search and retrieve specific contacts.
* Have a clear overview of all stored contacts.
* Delete unnecessary or outdated contacts.

## Flowchart

![Flowchart](/assets/images/contact-book-lucidchart.png)

# Features
* Add a New Contact: Allows users to enter contact details such as name, email, and phone number, and stores them in the Contact Book.
* Search for a Contact: Enables users to search for specific contacts by their name or email address, providing a list of matching contacts.
* Display All Contacts: Shows a well-organized list of all contacts, including their names, email addresses, and phone numbers.
* Delete a Contact: Allows users to remove a contact from the contact list if it is no longer needed.
* Exit program: Provides an option for users to exit the Contact Book application. This feature allows users to end their session and close the program.

## Existing Features
### Contact Book Menu
    
The Contact Book application provides a menu with the following options:
1.	Add a new contact
2.	Search for a contact
3.	Display all contacts
4.	Delete a contact
5.	Exit

To select an option, enter the corresponding number and press enter. After the selected action, you will remain on the current screen. From there, you can choose another action or enter a new command. If you enter an invalid option, an error message will be displayed.

### Add a new contact:
This feature allows you to enter details such as name, email, and phone number for a new contact. The input values are validated, and if they are correct, you will be prompted to confirm whether you want to add the contact to the Google Sheet. If you choose to proceed, the contact is added to the Google Sheet.

You will then have the option to return to the main menu or exit the program. If you enter incorrect information, an error message will be displayed, and you will be given the opportunity to re-enter the details.

### Search for a contact:
With this feature, you can search for a contact by entering their name or email address. The application searches through the contacts stored in the Google Sheet and displays any matches found. After the search, you can choose to search again or return to the main menu. If you make a mistake while entering the search term, an error message will be shown.

### Display all contacts:
This feature allows you to view a list of all the contacts stored in the Google Sheet. The program retrieves the contact information and presents it in an organized manner, including names, email addresses, and phone numbers. If there are no contacts available, a message will be displayed.

### Delete a contact:
This feature allows you to remove a contact from the contact list. You can enter the name or email address of the contact you wish to delete. The application will search for the contact in the Google Sheet and prompt you to confirm the deletion. If you choose to proceed, the contact will be removed from the Google Sheet. After deleting a contact, you can choose to search for another contact to delete, return to the main menu, or exit the program.

### Exit:
This option allows you to exit the Contact Book application. When selected, the program will end your session and display a goodbye message, thanking you for using the Contact Book.

# Technologies Used
The Contact Book application is built using the following technologies:

* Python: The core programming language used for implementing the application logic.
* gspread: A Python library used for interacting with Google Sheets API.
* google-auth: A Python library used for authentication with Google APIs.
* colorama: A Python library used for color highlighting in the command-line interface.

# Testing
The manual testing results for the contact book:

| Test menu input: | Result |
|--|--|
a. Testing menu input numbers 1-5:
Entered '1' as the menu input and verified that the program takes me to the "Add Contact" functionality.  | Pass |
Entered '2' as the menu input and verified that the program takes me to the "Search Contact" functionality. | Pass |
Entered '3' as the menu input and verified that the program takes me to the "Display All Contacts" functionality. | Pass |
Entered '4' as the menu input and verified that the program takes me to the "Delete Contact" functionality. | Pass |
Entered '5' as the menu input and verified that the program takes me to the "Update Contact" functionality.  | Pass |
b. Entered a number outside the range of 1-5 (e.g., '6', '10', '-1') and verified that an error message is displayed indicating an invalid input, and the program stays at the menu without proceeding | Pass |
c. Entered a non-numeric character (e.g., 'A', 'x', '#') and verified that an error message is displayed indicating an invalid input, and the program stays at the menu without proceeding.  | Pass |

| Test adding a new contact: | Result |
|--|--|
a. Created a test case where I provided valid contact information and verified that the contact is successfully added to Google Sheets. | Pass |
b. Created a test case where I provided invalid contact information (e.g., invalid name, invalid email address) and verified that the contact is not added and an appropriate error message is displayed.| Pass |
c. Tested the prompt "Do you want to add the contact?('Y' for yes or 'N' for no)" and verified that it correctly navigates to the appropriate place or displays an appropriate message. | Pass |

| Test searching for a contact: | Result |
|--|--|
a. Created a test case where I entered the name of an existing contact and verified that the contact information for the matching contact is displayed correctly. | Pass |
b. Created a test case where I searched for a contact that does not exist and verified that a message indicating that no contact was found is displayed. | Pass |
c. Tested the prompt "Do you want to search for another contact?('Y' for yes or 'N' for no)" and verified that it correctly navigates to the appropriate place or displays an appropriate message. | Pass |

| Test removing a contact: | Result |
|--|--|
a. Created a test case where I had multiple contacts saved in Google Sheets and verified that all contacts are displayed correctly with their names, email addresses, and phone numbers | Pass |
b. Created a test case where there were no contacts saved and verified that a message indicating that no contacts were found is displayed.  | Pass |
c. Tested the prompt "Press 'S' to go to start or 'E' to exit" and verified that it works correctly or displays an appropriate message. | Pass |

| Test displaying all contacts: | Result |
|--|--|
a. Created a test case where I entered the name of an existing contact and verified that the contact is successfully removed from Google Sheets. | Pass |
b. Created a test case where I attempted to remove a contact that does not exist and verified that an error message is displayed. | Pass |
c. Tested the prompt "Are you sure you want to delete this contact?('Y' for yes or 'N' for no)" and verified that it works correctly or displays an appropriate message.Test the prompt "Are you sure you want to delete this contact?('Y' for yes or 'N' for no)" and verify that it works correctly, or an appropriate message occurs. | Pass |
d. Tested the prompt "Do you want to search for another contact to delete?('Y' for yes or 'N' for no)" and verified that it works correctly or displays an appropriate error message.  | Pass |

| Test program exit: | Result |
|--|--|
Created a test case where I chose to exit the program and verified that it exits correctly without throwing any errors. | Pass |

# PEP8 Validator
PEP8 was used to validate the project and ensure there were no Python errors present.

![Pep8 validator](/assets/images/contact-book-pep8-verify.png)

# Development and Deployment
The Contact Book project was developed using the GitPod development environment. Version control and project tracking were managed through regular commits and pushes to GitHub. The initial setup of the GitPod environment was facilitated by a template provided by Code Institute. The live version of the project is deployed on the Heroku platform.

### Deploying on Heroku
To deploy the Contact Book program on [Heroku](https://dashboard.heroku.com/login), follow these steps:

1. Create an account and log in to the Heroku website.
2. Click on the "New" button and select "Create new app".
2. Enter a name for your app and choose the region. Then click the "Create App" button.
4. In the Settings tab, scroll down to the "Config vars" section and click on "Reveal Config Vars".
5. Add a new key-value pair. Enter "PORT" in the KEY section and "8000" as its value, then click "Add".
6. In the Buildpacks section, click on "Add buildpack".
7. Add the Python buildpack first, then add the Node.js buildpack.
8. Go to the Deploy tab and select "GitHub" as the deployment method.
9. Connect your app to your GitHub repository by searching for its name.
10. Choose whether you want to enable automatic or manual deploys. With automatic deploys, Heroku will build a new version of the app every time a change is pushed to the repository. Manual deploys require you to manually trigger the deployment process.
11. Once the deployment is finished, Heroku will provide you with a link to access your deployed app.

By following these steps, you will be able to deploy the Contact Book application on Heroku and make it accessible to users through the provided link. 

Link to the project: [Contact Book](https://contact--book-ebd067fbca38.herokuapp.com/)

# Credits

### Images
* Flowchart: The flowchart image used in the README is created using Lucidchart.
* Background image: The background image used in the project is sourced from Unsplash. [Link to the image on Unsplash](https://unsplash.com/photos/bGdiuIyN3Rs)

### Code References
* The Contact Book project uses the implementation of Google Sheets integration from the Love Sandwiches project by Code Institute. The code and concepts were adapted and modified to suit the requirements of the Contact Book application.

* The CSS code for the main background and terminal styling was adapted from the [American Pizza Order System project](https://github.com/useriasminna/american_pizza_order_system).