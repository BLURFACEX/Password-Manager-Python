import json
import getpass

# Function to save a new password
def save_password(data, service, username, password):
    data[service] = {"username": username, "password": password}

# Function to get a password for a given service
def get_password(data, service):
    entry = data.get(service)
    if entry:
        return entry["username"], entry["password"]
    else:
        return None

# Main function to run the password manager
def main():
    print("Welcome to the Password Manager!")

    # Load existing data or create an empty dictionary
    try:
        with open("passwords.json", "r") as data_file:
            try:
                data = json.load(data_file)
            except json.JSONDecodeError:
                print("Error decoding JSON. Creating a new data file.")
                data = {}
    except FileNotFoundError:
        print("Data file not found. Creating a new data file.")
        data = {}

    while True:
        print("\nPassword Manager Menu:")
        print("1. Save Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = getpass.getpass("Enter the password: ")
            save_password(data, service, username, password)
            print("Password saved successfully!")

        elif choice == "2":
            service = input("Enter the service name: ")
            credentials = get_password(data, service)
            if credentials:
                print(f"Username: {credentials[0]}\nPassword: {credentials[1]}")
            else:
                print("Password not found for the specified service.")

        elif choice == "3":
            # Save the data before exiting
            with open("passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=2)
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
