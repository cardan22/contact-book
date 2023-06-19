# Contact Book

Link to the project: [Contact Book](xxxx/)

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

# Features
* Add a New Contact: Allows users to enter contact details such as name, email, and phone number, and stores them in the Contact Book.
* Search for a Contact: Enables users to search for specific contacts by their name or email address, providing a list of matching contacts.
* Display All Contacts: Shows a well-organized list of all contacts, including their names, email addresses, and phone numbers.
* Delete a Contact: Allows users to remove a contact from the contact list if it is no longer needed.
* Exit program: Provides an option for users to exit the Contact Book application. This feature allows users to end their session and close the program.

## Existing Features

# Technologies Used
The Contact Book application is built using the following technologies:

* Python: The core programming language used for implementing the application logic.
* gspread: A Python library used for interacting with Google Sheets API.
* google-auth: A Python library used for authentication with Google APIs.
* colorama: A Python library used for color highlighting in the command-line interface.

# Testing

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

# Credits
