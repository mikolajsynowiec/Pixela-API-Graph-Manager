import requests
import re

username = ""
password = ""

pixela_endpoint = "https://pixe.la/v1/users"

def save_to_file(username, password):
    filename = "user_data.txt"
    data = f"Username: {username}, Password: {password}\n"

    # Open the file in append mode ('a'), create it if it doesn't exist
    with open(filename, "a") as file:
        file.write(data)
    print(f"User data saved to {filename}")

def validate_username(username):
    # Define the validation pattern
    pattern = r"^[a-z][a-z0-9-]{1,32}$"

    # Check if the username matches the pattern
    if re.match(pattern, username):
        return True  # Username is valid
    else:
        return False  # Username is invalid

def ask_yes_no(question):
    while True:
        response = input(question).strip().lower()
        if response in ['yes', 'no']:
            return response
        print("Invalid response. Please type 'yes' or 'no'.")

def create_user_account():
    global username, password
    print("Creating new account")

    # Prompt the user for a valid username
    while True:
        username = input("Enter username: ")
        if validate_username(username):
            break  # Valid username, exit the loop
        else:
            print("Invalid username. Please use only lowercase letters, digits, and hyphens, "
                  "starting with a letter, and ensure it's 2 to 33 characters long.")

    # Prompt the user for other details
    password = input("Enter password: ")
    agree_terms_of_use = ask_yes_no("Do you agree to the terms and conditions? (yes/no): ")
    not_minor = ask_yes_no("Are you an adult? (yes/no): ")

    # Validate responses
    if agree_terms_of_use != "yes":
        print("Account creation failed: You must agree to the terms of service.")
        return_to_menu()
        return
    if not_minor != "yes":
        print("Account creation failed: You must confirm that you are an adult.")
        return_to_menu()
        return

    # Create the user parameters for the API
    user_params = {
        "token": password,
        "username": username,
        "agreeTermsOfService": agree_terms_of_use,
        "notMinor": not_minor,
    }

    # Send a POST request to create the account
    pixela_endpoint = "https://your-api-endpoint.com"  # Replace with your actual API endpoint
    response_account = requests.post(url=pixela_endpoint, json=user_params)

    # Check the response from the API
    if response_account.ok:
        save_to_file(username, password)
        print("Account created successfully")
    else:
        # Display the error message from the API
        error_message = response_account.json().get("message", "Account creation failed for an unknown reason.")
        print(f"Account creation failed: {error_message}")

    # Return to the main menu or exit
    return_to_menu()

def create_graph():
    global username, password
    print("Login first to create graph")
    username = input("Enter username: ")
    password = input("Enter password: ")
    print("Creating graph")
    graph_id = input("Enter Graph ID: ")
    graph_name = input("Enter graph name: ")
    graph_units = input("Enter units (ex.minutes): ")
    graph_type = input("Enter graph type(int or float accepted): ")
    graph_color = input("Enter graph color(shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black)): ")

    graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

    graph_config ={
        "id": graph_id,
        "name": graph_name,
        "unit": graph_units,
        "type": graph_type,
        "color": graph_color,
    }

    headers = {
        "X-USER-TOKEN": password,
    }
    response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print("Graph created")
    return_to_menu()

def add_data():
    global username, password
    print("Login first to add data")
    username = input("Enter username: ")
    password = input("Enter password: ")
    print("Type graph id to add data")
    graph_id = input("Enter ID: ")
    post_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
    date=input("Enter the date (YYYYMMDD): ")
    quantity=input("Enter the quantity (min): ")
    add_graph ={
        "date": date,
        "quantity": quantity,
    }
    headers = {
        "X-USER-TOKEN": password,
    }

    response_data = requests.post(url = post_endpoint, json=add_graph, headers=headers)
    print("Data added successfully")
    return_to_menu()

def update_data():
    global username, password
    print("Login first to update data")
    username = input("Enter username: ")
    password = input("Enter password: ")
    print("Type graph id to add data")
    graph_id = input("Enter ID: ")
    date=input("Enter the date (YYYYMMDD): ")
    quantity=input("Enter the quantity (min): ")
    update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date}"

    add_graph ={
        "quantity": quantity,
    }
    headers = {
        "X-USER-TOKEN": password,
    }

    response_update = requests.put(url = update_endpoint, json=add_graph, headers=headers)
    print("Graph updated")
    return_to_menu()

def delete_graph():
    global username, password
    print("Login first to delete data")
    username = input("Enter username: ")
    password = input("Enter password: ")
    print("Type graph id to delete data")
    graph_id = input("Enter ID: ")
    delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
    headers = {
        "X-USER-TOKEN": password,
    }
    response_delete = requests.delete(url = delete_endpoint, headers=headers)
    print("Graph deleted")
    return_to_menu()

def return_to_menu():
    while True:
        choice = input("Would you like to return to the main menu or exit? (menu/exit): ").strip().lower()
        if choice == "menu":
            return  # Return to the main menu
        elif choice == "exit":
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 'menu' or 'exit'.")

def main_menu():
    while True:
        # Display menu options and get the user's choice
        print("Would you like to:")
        print("1 - Create account")
        print("2 - Create graph")
        print("3 - Add data to the graph")
        print("4 - Update data in your graph")
        print("5 - Delete graph")
        print("6 - Exit")

        try:
            question = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue  # Re-prompt the user

        # Perform the corresponding action based on the user's choice
        if question == 1:
            create_user_account()
        elif question == 2:
            create_graph()
        elif question == 3:
            add_data()
        elif question == 4:
            update_data()
        elif question == 5:
            delete_graph()
        elif question == 6:
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

main_menu()