# TASK 1: OPERATIONS ON TUPLE
# Create a Python program that:
# - Asks the user to input 5 fruit names and stores them in a tuple.
# - Displays the tuple.
# - Asks the user to enter a fruit name to search for, then displays whether the fruit exists in
# the tuple or not.
# - Counts and displays the number of occurrences of each fruit in the tuple
# TASK 1: OPERATIONS ON TUPLE

fruits = tuple(input(f"Enter fruit name {i+1}: ") for i in range(5))

print("\nFruits tuple:", fruits)

search_fruit = input("\nEnter a fruit name to search for: ")

if search_fruit in fruits:
    print(f"{search_fruit} exists in the tuple.")
else:
    print(f"{search_fruit} does not exist in the tuple.")

print("\nOccurrences of each fruit:")
for fruit in set(fruits):
    count = fruits.count(fruit)
    print(f"{fruit}: {count}")


# TASK 2: STUDENT DATA MANAGEMENT USING DICTIONARY
# Create a Python program to manage student data that:
# - Stores student data in a dictionary with the format:
# {
# "NIM1": {"Name": "Name1", "Major": "Major1", "GPA": 3.5},
# "NIM2": {"Name": "Name2", "Major": "Major2", "GPA": 3.8},
# ...
# }
# - Has an interactive menu with options to:
# - Add new student data
# - Display all student data
# - Search for student data based on NIM
# - Delete student data based on NIM
# The program should keep running until the user chooses to exit
# TASK 2: STUDENT DATA MANAGEMENT USING DICTIONARY

students = {}

def add_student():
    nim = input("Enter NIM: ")
    if nim in students:
        print("NIM already exists.")
        return
    name = input("Enter Name: ")
    major = input("Enter Major: ")
    try:
        gpa = float(input("Enter GPA: "))
    except ValueError:
        print("Invalid GPA. Please enter a number.")
        return
    students[nim] = {"Name": name, "Major": major, "GPA": gpa}
    print("Student added successfully.")

def display_students():
    if not students:
        print("No student data available.")
        return
    print("\nAll Student Data:")
    for nim, data in students.items():
        print(f"NIM: {nim}, Name: {data['Name']}, Major: {data['Major']}, GPA: {data['GPA']}")

def search_student():
    nim = input("Enter NIM to search: ")
    if nim in students:
        data = students[nim]
        print(f"Found: Name: {data['Name']}, Major: {data['Major']}, GPA: {data['GPA']}")
    else:
        print("Student not found.")

def delete_student():
    nim = input("Enter NIM to delete: ")
    if nim in students:
        del students[nim]
        print("Student deleted.")
    else:
        print("Student not found.")

while True:
    print("\nStudent Data Management Menu:")
    print("1. Add new student data")
    print("2. Display all student data")
    print("3. Search for student data by NIM")
    print("4. Delete student data by NIM")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")


# TASK 3: INVENTORY MANAGEMENT SYSTEM
# Create a Python program to manage item inventory in a warehouse. The program should
# include the following features:
# • Features:
# 1. Add New Item
# Prompts the user to enter item data in the format: Item_Name, Price, Stock. The data is
# stored in a dictionary:
# {
# "Item Name": (price, stock)
# }
# 2. Display All Items
# Displays a list of all items along with their prices and stock in table format.
# 3. Search for an Item
# Prompts the user to enter an item name, then displays the item's details. If the item is
# not found, show an appropriate message.
# 4. Update Item Stock
# Prompts the user to enter the item name and the new stock quantity. If the item is not
# found, show an appropriate message.
# 5. Delete Item
# Prompts the user to enter the item name to delete it from inventory. If the item is not
# found, show an appropriate message.
# 6. Data Analysis
# Displays:
# - The item with the highest and lowest price.
# - The total stock value (price × stock quantity for each item).
# 7. Exit Program
# TASK 3: INVENTORY MANAGEMENT SYSTEM

inventory = {}

def add_item():
    name = input("Enter item name: ")
    if name in inventory:
        print("Item already exists.")
        return
    try:
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
    except ValueError:
        print("Invalid input. Price must be a number and stock must be an integer.")
        return
    inventory[name] = (price, stock)
    print("Item added successfully.")

def display_items():
    if not inventory:
        print("No items in inventory.")
        return
    print("\nInventory List:")
    print("{:<20} {:<10} {:<10}".format("Item Name", "Price", "Stock"))
    for name, (price, stock) in inventory.items():
        print("{:<20} {:<10} {:<10}".format(name, price, stock))

def search_item():
    name = input("Enter item name to search: ")
    if name in inventory:
        price, stock = inventory[name]
        print(f"Item: {name}, Price: {price}, Stock: {stock}")
    else:
        print("Item not found.")

def update_stock():
    name = input("Enter item name to update stock: ")
    if name in inventory:
        try:
            new_stock = int(input("Enter new stock quantity: "))
        except ValueError:
            print("Invalid input. Stock must be an integer.")
            return
        price, _ = inventory[name]
        inventory[name] = (price, new_stock)
        print("Stock updated.")
    else:
        print("Item not found.")

def delete_item():
    name = input("Enter item name to delete: ")
    if name in inventory:
        del inventory[name]
        print("Item deleted.")
    else:
        print("Item not found.")

def data_analysis():
    if not inventory:
        print("No items for analysis.")
        return
    highest = max(inventory.items(), key=lambda x: x[1][0])
    lowest = min(inventory.items(), key=lambda x: x[1][0])
    total_value = sum(price * stock for price, stock in inventory.values())
    print(f"Highest price item: {highest[0]} (Price: {highest[1][0]})")
    print(f"Lowest price item: {lowest[0]} (Price: {lowest[1][0]})")
    print(f"Total stock value: {total_value}")

while True:
    print("\nInventory Management Menu:")
    print("1. Add New Item")
    print("2. Display All Items")
    print("3. Search for an Item")
    print("4. Update Item Stock")
    print("5. Delete Item")
    print("6. Data Analysis")
    print("7. Exit")
    choice = input("Choose an option (1-7): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        display_items()
    elif choice == "3":
        search_item()
    elif choice == "4":
        update_stock()
    elif choice == "5":
        delete_item()
    elif choice == "6":
        data_analysis()
    elif choice == "7":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")