#comments senteces
#


import tkinter as tk
from tkinter import messagebox
import csv
import os

# Function to load accommodations from the CSV file
def load_accommodations():
    accommodations = []
    if os.path.exists('accommodation.csv'):
        with open('accommodation.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row
            for row in reader:
                accommodations.append(row)
    return accommodations

# Function to save accommodation to the CSV file
def save_accommodation(name, location, price):
    # If the file doesn't exist, create it with a header row
    if not os.path.exists('accommodation.csv'):
        with open('accommodation.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Accommodation Name", "Location", "Price"])  # Header row

    # Append the accommodation data
    with open('accommodation.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, location, price])

# Function to add accommodation
def add_accommodation():
    name = entry_name.get()
    location = entry_location.get()
    price = entry_price.get()

    # Check if all fields are filled
    if not name or not location or not price:
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    try:
        price = float(price)  # Try converting price to a number
    except ValueError:
        messagebox.showerror("Error", "Price must be a number!")
        return

    # Save new accommodation
    save_accommodation(name, location, price)

    # Clear the input fields
    entry_name.delete(0, tk.END)
    entry_location.delete(0, tk.END)
    entry_price.delete(0, tk.END)

    # Update the listbox to show new accommodation
    update_listbox()

# Function to update listbox with accommodations
def update_listbox():
    listbox.delete(0, tk.END)  # Clear current list
    accommodations = load_accommodations()

    for acc in accommodations:
        listbox.insert(tk.END, f"{acc[0]} - {acc[1]} - ${acc[2]}")  # Display in format: Name - Location - Price

# Function to sort accommodations alphabetically by name
def sort_accommodations():
    accommodations = load_accommodations()
    accommodations.sort(key=lambda x: x[0].lower())  # Sort by name (case-insensitive)
    listbox.delete(0, tk.END)  # Clear current list

    for acc in accommodations:
        listbox.insert(tk.END, f"{acc[0]} - {acc[1]} - ${acc[2]}")  # Display in format: Name - Location - Price

# Create the main window
root = tk.Tk()
root.title("Accommodation App")

# Frame for input fields and button
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Name input field
label_name = tk.Label(frame, text="Accommodation Name:")
label_name.grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

# Location input field
label_location = tk.Label(frame, text="Location:")
label_location.grid(row=1, column=0, sticky="e")
entry_location = tk.Entry(frame)
entry_location.grid(row=1, column=1)

# Price input field
label_price = tk.Label(frame, text="Price per night ($):")
label_price.grid(row=2, column=0, sticky="e")
entry_price = tk.Entry(frame)
entry_price.grid(row=2, column=1)

# Add button
button_add = tk.Button(frame, text="Add Accommodation", command=add_accommodation)
button_add.grid(row=3, columnspan=2)

# Sort button
button_sort = tk.Button(frame, text="Sort Accommodations", command=sort_accommodations)
button_sort.grid(row=4, columnspan=2)

# Listbox to display accommodations
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(padx=10, pady=10)

# Load and display accommodations when the app starts
update_listbox()

# Start the Tkinter event loop
root.mainloop()
