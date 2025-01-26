Pixela Graph Management Tool

This project is a Python-based command-line tool for managing user accounts and graphs using the Pixela API. Pixela is an API service for creating and managing habit-tracking graphs. The tool allows users to perform tasks such as creating accounts, creating graphs, adding data, updating data, and deleting graphs.

Features

User Account Creation:

Create a new user account with a username and password.

Validate usernames to meet Pixela's requirements.

Save user credentials locally in a file (user_data.txt).

Graph Creation:

Create a new graph for habit tracking with customizable options like graph name, units, type, and color.

Add Data to Graphs:

Add daily data to an existing graph by specifying the graph ID, date, and quantity.

Update Graph Data:

Update existing data in a graph by specifying the graph ID, date, and the new quantity.

Delete Graphs:

Delete an existing graph by specifying the graph ID.

Interactive Menu:

A user-friendly menu to navigate between the features and return to the main menu or exit the program.

Prerequisites

Python 3.x

requests library for making API requests. Install it using:

pip install requests

How to Use

Step 1: Clone the Repository

Clone the project repository to your local machine or download the script file.

Step 2: Run the Program

Run the Python script in your terminal:

python script_name.py

Step 3: Interact with the Menu

Follow the interactive menu to:

Create a new account.

Manage graphs (create, add data, update data, or delete).

Menu Options:

Create Account

Prompts for a username and password.

Ensures username meets the required validation.

Saves account details locally.

Create Graph

Prompts for graph ID, name, units, type, and color.

Sends the graph creation request to the Pixela API.

Add Data to Graph

Prompts for graph ID, date (YYYYMMDD), and quantity.

Sends data to the specified graph.

Update Graph Data

Prompts for graph ID, date (YYYYMMDD), and updated quantity.

Updates the existing data.

Delete Graph

Prompts for graph ID and deletes the graph.

Exit

Exits the program.

Code Overview

Functions

validate_username(username)
Validates the username to ensure it adheres to Pixela's requirements.

save_to_file(username, password)
Saves user credentials to a local file (user_data.txt).

ask_yes_no(question)
Handles yes/no prompts for user confirmation.

create_user_account()
Handles account creation, validation, and API requests for registering a user.

create_graph()
Handles graph creation by prompting for graph details and making API requests.

add_data()
Adds daily data to a graph by prompting for graph ID, date, and quantity.

update_data()
Updates graph data by specifying graph ID, date, and the new quantity.

delete_graph()
Deletes an existing graph by specifying the graph ID.

return_to_menu()
Returns to the main menu or exits the program.

main_menu()
Displays the main menu and routes user input to the appropriate functions.

File Structure

script_name.py: Main Python script containing all functionality.

user_data.txt: File where user credentials are saved (created automatically).

API Reference

Endpoints

User Creation Endpoint: https://pixe.la/v1/users

Graph Creation Endpoint: https://pixe.la/v1/users/{username}/graphs

Add Data Endpoint: https://pixe.la/v1/users/{username}/graphs/{graphId}

Update Data Endpoint: https://pixe.la/v1/users/{username}/graphs/{graphId}/{date}

Delete Graph Endpoint: https://pixe.la/v1/users/{username}/graphs/{graphId}

Request Headers

All requests to graph endpoints require an X-USER-TOKEN header with the user's password as the token.

Notes

Replace https://your-api-endpoint.com in the code with the actual Pixela API endpoint.

Ensure sensitive data like passwords are handled securely.

This tool is designed for educational purposes. Enhance security if deploying in a production environment.
