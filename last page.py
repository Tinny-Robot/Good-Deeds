import tkinter as tk
from tkinter import ttk

def submit_form():
    # Gather the form data and process it as needed
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    # ... Process other form data here ...

    # For demonstration purposes, let's print the data to the console
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    # ... Print other form data here ...

    # You can add further processing or validation here as needed

    # Optionally, you could reset the form fields after submission
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set('')
    duration_var.set(0)

# Create the main application window
root = tk.Tk()
root.title("Diagnostic Form")

# Create a canvas and a scrollbar for the form
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas to hold the form elements
form_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=form_frame, anchor="nw")

# Patient Information
tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Age:").grid(row=1, column=0, sticky="e")
age_entry = tk.Entry(form_frame)
age_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Gender:").grid(row=2, column=0, sticky="e")
gender_var = tk.StringVar()
gender_choices = ["Male", "Female", "Other"]
gender_dropdown = tk.OptionMenu(form_frame, gender_var, *gender_choices)
gender_dropdown.grid(row=2, column=1, pady=5)

# Symptoms
symptoms_frame = tk.Frame(form_frame)
symptoms_frame.grid(row=3, columnspan=2, pady=10)

tk.Label(symptoms_frame, text="Symptoms:").pack()

symptoms = ["Fever", "Cough", "Shortness of breath", "Fatigue", "Headache",
            "Muscle aches", "Sore throat", "Nausea or vomiting", "Diarrhea", "Rash"]
symptom_vars = []
for i, symptom in enumerate(symptoms):
    var = tk.IntVar()
    tk.Checkbutton(symptoms_frame, text=symptom, variable=var).pack(anchor="w")
    symptom_vars.append(var)

# Duration (progress bar)
duration_frame = tk.Frame(form_frame)
duration_frame.grid(row=4, columnspan=2, pady=10)

tk.Label(duration_frame, text="Duration:").pack()
duration_var = tk.DoubleVar()
duration_progress = ttk.Progressbar(duration_frame, variable=duration_var, maximum=100)
duration_progress.pack(fill=tk.X)

# Exposure (textarea)
exposure_frame = tk.Frame(form_frame)
exposure_frame.grid(row=5, columnspan=2, pady=10)

tk.Label(exposure_frame, text="Exposure:").pack()
exposure_text = tk.Text(exposure_frame, height=5, width=40)
exposure_text.pack()

# Medical Background
tk.Label(form_frame, text="Medical Background:").grid(row=6, columnspan=2, pady=5)
medical_background_text = tk.Text(form_frame, height=5, width=40)
medical_background_text.grid(row=7, columnspan=2, pady=5)

# Additional Notes
tk.Label(form_frame, text="Additional Notes:").grid(row=8, columnspan=2, pady=5)
additional_notes_text = tk.Text(form_frame, height=5, width=40)
additional_notes_text.grid(row=9, columnspan=2, pady=5)

# Doctors Comment
tk.Label(form_frame, text="Doctor's Comment:").grid(row=10, columnspan=2, pady=5)
doctors_comment_text = tk.Text(form_frame, height=5, width=40)
doctors_comment_text.grid(row=11, columnspan=2, pady=5)

# Submit Button
submit_button = tk.Button(form_frame, text="Submit", command=submit_form)
submit_button.grid(row=12, columnspan=2, pady=10)

# Update the canvas scroll region when the form_frame size changes
form_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run the application
root.mainloop()
