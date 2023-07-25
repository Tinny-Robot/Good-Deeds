import tkinter as tk
from tkinter import Menu, simpledialog, messagebox
from PIL import Image, ImageTk
import csv


class ImageFrameWithMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GOOD DEEDS PHARMACEUTICAL")

        self.image_path = "background.jpg"  # Replace with your image file path


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


    def create_menu(self):
        menubar = Menu(self.root)

        # First menu button
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="LOG IN", command=self.menu1_option1)
        menu1.add_command(label="SIGN UP", command=self.menu1_option2)
        menubar.add_cascade(label="Medical Official", menu=menu1)

        # Second menu button
        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="LOG IN", command=self.menu2_option1)
        menu2.add_command(label="SIGN UP", command=self.menu2_option2)
        menubar.add_cascade(label="Patient", menu=menu2)

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
        

    def user_login(self, username,password ):
        print(username.get(), password.get())
        data = []
        with open("users.csv", "r+", newline="") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                data.append(i)
        # data.append([username.get(), password.get(), False])
        for i in data:
            if i[0] == username.get() and i[1] == password.get():
                self.destroy(self.frame)
                print(i)
                break
        else:
            messagebox.showerror('error', 'rest')



    def user_signup(self, username,password ):
        print(username.get(), password.get())
        data = []
        with open("users.csv", "r+", newline="") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                data.append(i)
        print(data)

        for i in data:
            print(i)
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
        print(username.get(), password.get())
        data = []
        with open("users.csv", "r+", newline="") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                data.append(i)
        # data.append([username.get(), password.get(), False])
        for i in data:
            if i[0] == username.get() and i[1] == password.get():
                messagebox.showinfo('yes', 'Login')
                print(i)
                break
        else:
            messagebox.showerror('error', 'rest')



    def doc_signup(self, username,password ):
        print(username.get(), password.get())
        data = []
        with open("users.csv", "r+", newline="") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                data.append(i)
        print(data)

        for i in data:
            print(i)
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

        tk.Label(login_frame).pack()
        tk.Button(login_frame, text="Login", command=lambda: self.user_login(username,password )).pack()


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
