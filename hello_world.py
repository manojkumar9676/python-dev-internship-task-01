# hello_world.py
# This program prints intern details using user input

# Import datetime module to get today's date
from datetime import date

# Ask user for their name
name = input("Enter your name: ")

# Ask user for internship role
role = input("Enter your internship role: ")

# Get today's date
today_date = date.today()

# Print the details
print("\n--- Intern Details ---")
print("Name:", name)
print("Internship Role:", role)
print("Date:", today_date)
