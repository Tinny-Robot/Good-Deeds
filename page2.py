import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk  
import datetime

def on_review_button_click(row):
    result = simpledialog.askstring("Review", "Yes or No?", parent=table_frame)
    if result:
        # Do something with the result, e.g., update the table data
        # For now, we'll just print the result for demonstration purposes
        print(f"Review for row {row}: {result}")

def on_edit_button_click(row):
    # Implement the action you want when the Edit button is clicked
    # For now, we'll just print a message for demonstration purposes
    print(f"Edit row {row}")

def on_add_row_button_click():
    # Add a new row to the table
    # For now, we'll add a placeholder data for demonstration purposes
    updated = datetime.datetime.now().strftime("%m-%d  %H:%M:%S")
    new_row_data = ["New Review", updated]
    table_data.append(new_row_data)
    update_table()

def update_table():
    global add_row_button  # Make add_row_button a global variable

    # Clear the existing table
    for widget in table_frame.winfo_children():
        widget.grid_forget()

    # Create the table headers
    headers = ["Review", "Date and Time", "Edit"]
    for col, header in enumerate(headers):
        tk.Label(table_frame, text=header, bg="lightgray", relief=tk.RIDGE, width=20).grid(row=0, column=col, sticky="nsew")

    if table_data:
        # Create the table rows
        for row, (review, datetime) in enumerate(table_data, start=1):
            tk.Label(table_frame, text=review, bg="white", relief=tk.RIDGE, width=20).grid(row=row, column=0, sticky="nsew")
            tk.Label(table_frame, text=datetime, bg="white", relief=tk.RIDGE, width=20).grid(row=row, column=1, sticky="nsew")
            review_button = tk.Button(table_frame, text="Review", command=lambda r=row: on_review_button_click(r))
            review_button.grid(row=row, column=2, sticky="nsew")
            edit_button = tk.Button(table_frame, text="Edit", command=lambda r=row: on_edit_button_click(r))
            edit_button.grid(row=row, column=3, sticky="nsew")
    else:
        tk.Label(table_frame, text="No Entry yet", bg="white", fg="red").grid(sticky="nsew")


    # Add the "Add Row" button at the end of the table
    add_row_button = tk.Button(table_frame, text="Add Row", command=on_add_row_button_click)
    add_row_button.grid(row=len(table_data) + 1, column=0, columnspan=4, pady=(10, 0))

# Sample data for the table (replace this with your actual data)
table_data = [
        # Add more rows as needed
]

# Create the main application window
root = tk.Tk()
root.title("Table GUI with Image Background")

# Load the background image
background_image = Image.open("pathtoframe-background.jpg")  # Replace with your image path
background_photo = ImageTk.PhotoImage(background_image)
background_image = background_image.resize((1700, 1300), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold the table
table_frame = tk.Frame(root, bg="white")
table_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create the table
update_table()

# Adjust row and column weights to make the table expandable
for i in range(4):
    table_frame.grid_columnconfigure(i, weight=1)
table_frame.grid_rowconfigure(0, weight=1)

root.mainloop()
