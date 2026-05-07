import random
import string
import json
import os

# File to store data
FILE_NAME = "url_data.json"

# Load existing data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)

# Generate unique short code
def generate_code(data, length=6):
    chars = string.ascii_letters + string.digits
    
    while True:
        code = "".join(random.choice(chars) for _ in range(length))
        if code not in data:
            return code

# Shorten URL
def shorten_url(data, long_url):
    # Check duplicate
    for code, url in data.items():
        if url == long_url:
            return code

    code = generate_code(data)
    data[code] = long_url
    save_data(data)
    return code

# Retrieve original URL
def retrieve_url(data, code):
    return data.get(code, None)

# Display all URLs
def show_all(data):
    if not data:
        print("No URLs stored.")
        return

    for code, url in data.items():
        print(f"{code} → {url}")

# Main program
def main():
    data = load_data()

    while True:
        print("\n--- URL Shortener ---")
        print("1. Shorten URL")
        print("2. Retrieve URL")
        print("3. Show all URLs")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            long_url = input("Enter long URL: ")
            code = shorten_url(data, long_url)
            print("Short URL: short.ly/" + code)

        elif choice == "2":
            code = input("Enter short code: ")
            url = retrieve_url(data, code)

            if url:
                print("Original URL:", url)
            else:
                print("URL not found!")

        elif choice == "3":
            show_all(data)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()