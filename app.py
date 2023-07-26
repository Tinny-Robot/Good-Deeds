import tkinter as tk
from tkinter import Menu, simpledialog, messagebox,ttk
from PIL import Image, ImageTk
import csv
import datetime

class ImageFrameWithMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GOOD DEEDS PHARMACEUTICAL")

        self.image_path = "background.jpg"  # Replace with your image file path
        self.table_data = []

                # Load the image
        image = Image.open(self.image_path)
        image = image.resize((1700, 1300))
        photo = ImageTk.PhotoImage(image)

        # Create the frame with the image background
        frame = tk.Frame(self.root, width=image.width, height=image.height)
        frame.pack_propagate(False)  # Prevent frame from adjusting to the content
        frame.pack()
        self.frame = frame
        self.photo = photo

        # Add the image to the frame
        label = tk.Label(frame, image=photo)
        label.pack()

        # Save a reference to the image to prevent it from being garbage collected
        label.image = photo

        self.frame = frame

        self.create_menu()
        self.create_widgets(frame)
        self.table_frame = tk.Frame(root, bg="white")

    def submit_form(self, canvas):
        pass

    def add_form(self, frame):
        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        form_frame = tk.Frame(canvas)

        canvas.create_window((0, 0), window=form_frame, anchor="nw")
        canvas.config(yscrollcommand=scrollbar.set)

        form_frame = frame
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

        symptoms = ["Fever", "Cough", "Headache","vomiting", "Diarrhea", "Rash"]
        symptom_vars = []
        for i, symptom in enumerate(symptoms):
            var = tk.IntVar()
            tk.Checkbutton(symptoms_frame, text=symptom, variable=var).pack(anchor="w")
            symptom_vars.append(var)

        # Additional Notes
        tk.Label(form_frame, text="Additional Notes:").grid(row=8, columnspan=2, pady=5)
        additional_notes_text = tk.Text(form_frame, height=5, width=40)
        additional_notes_text.grid(row=9, columnspan=2, pady=5)

        # Doctors Comment
        tk.Label(form_frame, text="Doctor's Comment:").grid(row=10, columnspan=2, pady=5)
        doctors_comment_text = tk.Text(form_frame, height=5, width=40)
        doctors_comment_text.grid(row=11, columnspan=2, pady=5)

        # Submit Button
        submit_button = tk.Button(form_frame, text="Submit", command=self.submit_form)
        submit_button.grid(row=12, columnspan=2, pady=10)

        # Update the canvas scroll region when the form_frame size changes
        form_frame.update_idletasks()



    def on_review_button_click(self, row):
        result = simpledialog.askstring("Review", "Yes or No?", parent=self.table_frame)
        if result:
            # Do something with the result, e.g., update the table data
            # For now, we'll just print the result for demonstration purposes
            print(f"Review for row {row}: {result}")

    # def on_edit_button_click(self,row):
    #     # Implement the action you want when the Edit button is clicked
    #     # For now, we'll just print a message for demonstration purposes
    #     # print(f"Edit row {row}")

    def on_add_row_button_click(self,):
        # updated = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        # new_row_data = ["New Review", updated]
        # self.table_data.append(new_row_data)
        # self.update_table()
        self.destroy(self.frame)
        self.table_frame.place_forget()
        self.add_form(self.frame)
        

    def update_table(self,):
        global add_row_button  # Make add_row_button a global variable

        # Clear the existing table
        for widget in self.table_frame.winfo_children():
            widget.grid_forget()

        # Create the table headers
        headers = ["Review", "Date and Time", "Edit"]
        for col, header in enumerate(headers):
            tk.Label(self.table_frame, text=header, bg="lightgray", relief=tk.RIDGE, width=20).grid(row=0, column=col, sticky="nsew")

        if self.table_data:
            # Create the table rows
            for row, (review, datetime) in enumerate(self.table_data, start=1):
                tk.Label(self.table_frame, text=review, bg="white", relief=tk.RIDGE, width=20).grid(row=row, column=0, sticky="nsew")
                tk.Label(self.table_frame, text=datetime, bg="white", relief=tk.RIDGE, width=20).grid(row=row, column=1, sticky="nsew")
                review_button = tk.Button(self.table_frame, text="Review", command=lambda r=row: self.on_review_button_click(r))
                review_button.grid(row=row, column=2, sticky="nsew")
                # edit_button = tk.Button(self.table_frame, text="Edit", command=lambda r=row: self.on_edit_button_click(r))
                # edit_button.grid(row=row, column=3, sticky="nsew")
        else:
            tk.Label(self.table_frame, text="No Entry yet", bg="white", fg="red").grid(sticky="nsew")


        # Add the "Add Row" button at the end of the table
        add_row_button = tk.Button(self.table_frame, text="Add Report", command=self.on_add_row_button_click)
        add_row_button.grid(row=len(self.table_data) + 1, column=0, columnspan=4, pady=(10, 0))


    def create_menu(self):
        menubar = Menu(self.root)

        # First menu button
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="LOG IN", command=self.menu1_option1)
        menu1.add_command(label="SIGN UP", command=self.menu1_option2)
        menubar.add_cascade(label="Patient", menu=menu1)

        # Second menu button
        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="LOG IN", command=self.menu2_option1)
        menu2.add_command(label="SIGN UP", command=self.menu2_option2)
        menubar.add_cascade(label="Medical Official", menu=menu2)

        # Change menu bar position to top-right
        self.root.config(menu=menubar)

    def create_widgets(self, frame):

        # Add text to the center of the main window
        text = " GOOD DEEDS PHARMACEUTICAL"
        text_label = tk.Label(frame, text=text, font=("Helvetica", 40))
        text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Add a label below the center text
        label_below_text = tk.Label(frame, text="Welcome to our pharmaceutical website, where we are dedicated to advancing healthcare and well-being for all.", font=("Helvetica", 12))
        label_below_text.place(relx=0.5, rely=0.6, anchor=tk.CENTER)


    def destroy(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

                # Add the image to the frame
        label = tk.Label(frame, image=self.photo)
        label.pack()

        # Save a reference to the image to prevent it from being garbage collected
        label.image = self.photo
        
    def get_info(self, user):
        data = []
        with open("data.csv", "r+", newline="") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                data.append(i)
        this = []
        for i in data:
            if user == i[0]:
                this.append(i)
        
        for i,j in enumerate(this):
            self.table_data.append([str(user)+" "+str(i+1), j[1],])

        

    def user_login(self, username,password ):
        # print(username.get(), password.get())
        data = []
        with open("users.csv", "r+", newline="") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                data.append(i)
        # data.append([username.get(), password.get(), False])
        for i in data:
            if i[0] == username.get() and i[1] == password.get():
                self.destroy(self.frame)
                self.table_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                self.table_data = []
                self.get_info(username.get())
                self.update_table()
                break
        else:
            messagebox.showerror('Login Error', 'Incorrect Details')



    def user_signup(self, username,password ):
        # print(username.get(), password.get())
        data = []
        with open("users.csv", "r+", newline="") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                data.append(i)
        # print(data)

        for i in data:
            # print(i)
            if i[0] == username.get():
                messagebox.showerror("Error", "User Already Exist")
                return 0
            
        data.append([username.get(), password.get(), False])
        
        with open("users.csv", "r+", newline="") as csvfile:
            file = csv.writer(csvfile)
            for i in data:
                file.writerow(i)
        
        messagebox.showinfo('Success', 'Successfull created account')
        self.user_login(username, password)

        return
    
    def doc_login(self, username,password ):
        # print(username.get(), password.get())
        data = []
        with open("users.csv", "r+", newline="") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                data.append(i)
        # data.append([username.get(), password.get(), False])
        for i in data:
            if i[0] == username.get() and i[1] == password.get():
                # print(i[0])
                if i[-1] != "True":
                    messagebox.showerror('Login Error', 'Incorrect Details')
                    return
                self.table_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                self.destroy(self.frame)
                self.update_table()
                # messagebox.showinfo('yes', 'Login')
                # print(i)
                break
        else:
            messagebox.showerror('Login Error', 'Incorrect Details')



    def doc_signup(self, username,password ):
        print(username.get(), password.get())
        data = []
        with open("users.csv", "r+", newline="") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                data.append(i)
        # print(data)

        for i in data:
            # print(i)
            if i[0] == username.get():
                messagebox.showerror("Error", "User Already Exist")
                return 0
            
        data.append([username.get(), password.get(), True])
        
        with open("users.csv", "r+", newline="") as csvfile:
            file = csv.writer(csvfile)
            for i in data:
                file.writerow(i)
        
        messagebox.showinfo('Success', 'Successfull created account')
        self.doc_login(username, password)

        return


    def menu1_option1(self):
        login_frame = tk.Toplevel(self.root)
        login_frame.title("LOG IN")
        login_frame.geometry("400x200")
        username = tk.StringVar()
        password = tk.StringVar()

        tk.Label(login_frame, text="Username:").pack()
        tk.Entry(login_frame, textvariable=username).pack()
        tk.Label(login_frame, text="Password:").pack()
        tk.Entry(login_frame, textvariable=password, show="*").pack()
        def kill():
            login_frame.destroy()
            login_frame.update()

        tk.Label(login_frame).pack()
        tk.Button(login_frame, text="Login", command=lambda: [self.user_login(username,password ),  ]).pack()


    def menu1_option2(self):
        signup_frame = tk.Toplevel(self.root)
        signup_frame.title("SIGN UP")
        signup_frame.geometry("400x200")
        username = tk.StringVar()
        password = tk.StringVar()

        tk.Label(signup_frame, text="Username:").pack()
        tk.Entry(signup_frame, textvariable=username).pack()
        tk.Label(signup_frame, text="Password:").pack()
        tk.Entry(signup_frame, textvariable=password, show="*").pack()

        tk.Label(signup_frame).pack()
        tk.Button(signup_frame, text="Sign UP", command=lambda: self.user_signup(username,password )).pack()

    def menu2_option1(self):
        signup_frame = tk.Toplevel(self.root)
        signup_frame.title("SIGN UP")
        signup_frame.geometry("400x200")
        username = tk.StringVar()
        password = tk.StringVar()

        tk.Label(signup_frame, text="Username:").pack()
        tk.Entry(signup_frame, textvariable=username).pack()
        tk.Label(signup_frame, text="Password:").pack()
        tk.Entry(signup_frame, textvariable=password, show="*").pack()

        tk.Label(signup_frame).pack()
        tk.Button(signup_frame, text="Login", command=lambda: self.doc_login(username,password )).pack()
       
    def menu2_option2(self):
        signup_frame = tk.Toplevel(self.root)
        signup_frame.geometry("400x200")
        signup_frame.title("SIGN UP")
        username = tk.StringVar()
        password = tk.StringVar()

        tk.Label(signup_frame, text="Username:").pack()
        tk.Entry(signup_frame, textvariable=username).pack()
        tk.Label(signup_frame, text="Password:").pack()
        tk.Entry(signup_frame, textvariable=password, show="*").pack()

        tk.Label(signup_frame).pack()
        tk.Button(signup_frame, text="Login", command=lambda: self.doc_signup(username,password )).pack()



if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFrameWithMenuApp(root)
    root.mainloop()
