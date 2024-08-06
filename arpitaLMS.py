import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import font as tkfont
from tkinter import ttk
from tkinter import PhotoImage
import webbrowser
import json
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for development and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(__file__)              # PyInstaller creates a temp folder and stores the path in _MEIPASS (created to help in making.exe)
    return os.path.join(base_path, relative_path)          # In development mode, the file is in the current directory


# Admin credentials
ADMIN_USERNAME = "arpita"       
ADMIN_PASSWORD = "password"

# File paths for storing data
BOOKS_FILE = "books.json"
AUTHORS_FILE = "authors.json"
BORROWERS_FILE = "borrowers.json"
DUES_FILE = "dues.json"

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.configure(bg="#433987")
        self.root.geometry("1200x700")
        
        # Load the logo image
        logo_path = resource_path('logo.png')
        self.logo_image = PhotoImage(file=logo_path)
        self.root.iconphoto(False, self.logo_image)
    
        # Initialize data
        self.books_data = self.load_json('books.json')
        self.authors_data = self.load_json('authors.json')
        self.borrowers_data = self.load_json('borrowers.json')
        self.dues_data = self.load_json('dues.json')
        

        # Initialize data
        self.books_data = []
        self.authors_data = []
        self.borrowers_data = []
        self.due_data = []
        self.borrowers_data = []

        
        self.load_data()  # Load other data
        
        self.create_welcome_widgets()
        
    # -------------------------------------------------------------- Here is the Welcome page (front) ---------------------------------------------------------------
        
    def create_welcome_widgets(self):
        # Create the welcome frame
        self.welcome_frame = tk.Frame(self.root, bg="#433987")
        self.welcome_frame.pack(pady=10)            

        # Add welcome text and button
        tk.Label(self.welcome_frame, text="A Project Report on Library Management System", bg="#433987", fg="white", font=("Comic Sans MS", 30)).pack(pady=50)
        tk.Label(self.welcome_frame, text="Diploma in Computer Application", bg="#433987", fg="white", font=("Consolas", 20)).pack(pady=0)
        tk.Label(self.welcome_frame, text="2023-2024", bg="#433987", fg="white", font=("Arial", 20)).pack(pady=5)
        self.enter_button = tk.Button(self.welcome_frame, text="Enter", command=self.go_to_login_selection, bg="#c2d9f2", fg="#040f07", relief="raised", font=("Arial", 16), bd=15)
        
        self.enter_button.pack(pady=30)                                
        #This button send to login selection
        
        tk.Label(self.welcome_frame, text="Guided by -                                                                                                                                                       Submitted by-", bg="#433987", fg="white", font=("Arial", 14)).pack(pady=0)
        tk.Label(self.welcome_frame, text="Suman sir                                                                                 Arpita Bhadauriya ", bg="#433987", fg="white", font=("Times New Roman", 25)).pack(pady=0)
        tk.Label(self.welcome_frame, text="CV Raman University \n Bilaspur", bg="#433987", fg="white", font=("Arial", 20)).pack(pady=20)
        tk.Label(self.welcome_frame, text="Registered Study Center -", bg="#433987", fg="white", font=("Consolas", 16)).pack(pady=0)
        tk.Label(self.welcome_frame, text="Universal Computer Education\n Station maroda,Bhilai", bg="#433987", fg="white", font=("Arial", 20)).pack(pady=3)


    def go_to_login_selection(self):
        self.welcome_frame.pack_forget()          # navigate to user selection page
        self.create_login_selection_widgets()   
        
    # ------------------------------------------------------------------ Page 2 (User & Admin) selection page -----------------------------------------------------------
        
    def create_login_selection_widgets(self):
         # Ensure previous widgets are hidden
        for widget in self.root.winfo_children():
            widget.pack_forget()
            
        self.login_selection_frame = tk.Frame(self.root, bg="#433987") 
        self.login_selection_frame.pack(pady=20)                
        
        tk.Label(self.login_selection_frame, text="A Project Report on Library Management System", bg="#433987", fg="#fff", font=("Comic Sans MS", 30, "bold")).pack(pady=30)
        tk.Button(self.login_selection_frame, text="Library Admin", command=self.go_to_admin_login, width=20, height=2, bg="#ff5447", relief="raised", font=("Arial", 13, "bold")).pack(pady=15)
        tk.Button(self.login_selection_frame, text="Students Enter here", command=self.enter_as_user, width=50, height=3, bg="#5effd4", relief="raised", font=("Arial", 14, "bold")).pack(pady=18)
        
        logo_path = resource_path('logo.png')
        self.logo_image = PhotoImage(file=logo_path)

        # Create a label to display the logo
        logo_label = tk.Label(self.login_selection_frame, image=self.logo_image, bg="#433987")
        logo_label.pack(pady=20)
        logo_label.bind("<Button-1>", self.open_link)

    def open_link(self, event):
        # Open web browser
        webbrowser.open("https://cvru.ac.in/")

    def go_to_admin_login(self):
        self.login_selection_frame.pack_forget() # navigate to admin login
        self.create_admin_login_widgets()
        
    def enter_as_user(self):
        self.login_selection_frame.pack_forget() # navigate to user page
        self.create_user_section()
        
        
    # ----------------------------------------------------------- Page 3 (admin credential input page) -------------------------------------------------------
        
    def create_admin_login_widgets(self):
        
        self.admin_login_frame = tk.Frame(self.root, bg="#433987")
        self.admin_login_frame.grid(row=0, column=0, padx=20, pady=20)

        tk.Label(self.admin_login_frame, text="- Library Management Login -", bg="#433987", fg="#fff", font=("Comic Sans MS", 30, "bold")).grid(row=0, column=0, columnspan=2, pady=30)
        
        # Username label and entry
        tk.Label(self.admin_login_frame, text="Username:", bg="#433987", fg="white", font=("Arial", 16)).grid(row=1, column=0, pady=5, padx=10, sticky='e')
        self.username_entry = tk.Entry(self.admin_login_frame, font=("Arial", 16))
        self.username_entry.grid(row=1, column=1, pady=10, padx=10)
        
        #password label and entry
        tk.Label(self.admin_login_frame, text="Password:", bg="#433987", fg="white", font=("Arial", 16)).grid(row=2, column=0, pady=5, padx=10, sticky='e')
        self.password_entry = tk.Entry(self.admin_login_frame, show="*", font=("Arial", 16))
        self.password_entry.grid(row=2, column=1, pady=10, padx=10)
        
        #login buttons for enter
        tk.Button(self.admin_login_frame, text="Admin Login", command=self.check_admin_credentials, width=20, height=3, bg="#ff6b7f", relief="raised", font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=2, pady=15)
        #go back button
        tk.Button(self.admin_login_frame, text="Go back to USER", command=self.go_back_to_login_selection, width=50, height=3, bg="#5effd4", relief="raised", font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=2, pady=15)
        
        # Configure grid to ensure proper spacing
        for i in range(5):
            self.admin_login_frame.grid_rowconfigure(i, weight=1)
            self.admin_login_frame.grid_columnconfigure(i, weight=1)

        
    def check_admin_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD: # check for credentials
            self.admin_login_frame.grid_forget()                      # send to inside admin workplace
            self.create_admin_section()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            

    def go_back_to_login_selection(self):
        self.admin_login_frame.grid_forget()             #Navigation(Shift admin" login frame to user selection frame)
        self.create_login_selection_widgets()
        
    #----------------------------------------------------------------- Admin (Library management = admin) ------------------------------------------------

    def create_admin_section(self):

        self.admin_frame = tk.Frame(self.root, bg="#433987")
        self.admin_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        #label frame
        label = tk.Label(self.admin_frame, text="Library Administrator", bg="#433987", fg="white", font=("Arial", 30, "bold"))
        label.grid(row=0, column=0, columnspan=2, pady=2)
 
        # Define buttons
        buttons = [
            ("Books Management", self.show_books),
            ("Authors List", self.show_authors),
            ("Borrowers List / Return book", self.show_borrowers),
            ("Dues Payment Section", self.show_due),
            ("Logout admin", self.logout)
        ]
    
        # Setup buttons in the buttons_frame using grid
        self.setup_buttons(self.admin_frame, buttons)

    def setup_buttons(self, frame, buttons):
        # Define grid column and row counters
        row = 1
        col = 0

        for text, command in buttons:
            button = tk.Button(frame, text=text, command=command, width=25, height=4, bg="#c2d9f2", relief="raised", font=("Arial", 14, "bold"))
            button.grid(row=row, column=col, padx=2, pady=2)

            # Move to the next column
            col += 1
            # Move to the next row if there are more than 2 columns
            if col > 1:
                col = 0
                row += 1
                
        # Center the buttons_frame content
        for i in range(row + 1):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(col + 1):
            frame.grid_columnconfigure(j, weight=1)

                
    def logout(self):
        self.admin_frame.pack_forget()        #Navigation (shift from admin frame to welcome frame"starting")
        self.create_welcome_widgets()
        self.welcome_frame.pack(pady=20)

    # ---------------------------------------------------------------------- Book Page ----------------------------------------------------------------------------------
    def show_books(self):
        
        self.admin_frame.pack_forget()
        self.books_frame = tk.Frame(self.root, bg="#16a167")
        self.books_frame.pack(fill='both', expand=True)

        buttons = [
            ("Remove Book", self.remove_book),
            ("Add Book", self.add_book),            # Create buttons and place them in a grid
            ("Borrow Book", self.borrow_book),
            ("Back", self.go_back_from_books)
        ]
        
        row = 0
        col = 0
        for text, command in buttons:
            button = tk.Button(self.books_frame, text=text, command=command, width=20, height=3, bg="#16a167", relief="raised", font=("Arial", 12, "bold"))
            button.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col > 1:
                col = 0
                row += 1

        # Create and place the Treeview widget in a grid
        self.books_table = ttk.Treeview(self.books_frame, columns=("ID", "Name", "Author"), show='headings')
        self.books_table.heading("ID", text="Book ID", anchor=tk.W)
        self.books_table.heading("Name", text="Book Name", anchor=tk.W)
        self.books_table.heading("Author", text="Author", anchor=tk.W)
        self.books_table.column("ID", width=100, anchor=tk.W)
        self.books_table.column("Name", width=400, anchor=tk.W)
        self.books_table.column("Author", width=300, anchor=tk.W)
        self.books_table.grid(row=row, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
         # Adjust the row and column weights so the Treeview expands with the window
        self.books_frame.grid_rowconfigure(row, weight=1)
        self.books_frame.grid_columnconfigure(0, weight=1)
        self.books_frame.grid_columnconfigure(1, weight=1)

        self.update_books_table()
        

    def update_books_table(self):
         # Clear the current contents of the Treeview
        for item in self.books_table.get_children():
            self.books_table.delete(item)
            
        self.load_data()
        # Sort books data by ID in ascending order
        sorted_books = sorted(self.books_data, key=lambda x: int(x["ID"]))

        # Insert sorted books into the Treeview
        for book in sorted_books:
            self.books_table.insert("", "end", values=(book["ID"], book["Name"], book["Author"]))
            
    def go_back_from_books(self):
        self.books_frame.pack_forget()
        self.create_admin_section()     #Navigation (shift books frame to admin)
        self.admin_frame.pack(pady=20)
        
    #------------------------------------------------------------------ Add Book button ---------------------------------------------------------------------------
    
    def add_book(self):
        # Open dialog to enter book details
        add_book_dialog = tk.Toplevel(self.root)
        add_book_dialog.title("Add Book")
        add_book_dialog.configure(bg="#16a167")

        tk.Label(add_book_dialog, text="Enter Book ID:", bg="#16a167", fg="white").grid(row=0, column=0, padx=10, pady=10)
        book_id_entry = tk.Entry(add_book_dialog)
        book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_book_dialog, text="Enter Book Name:", bg="#16a167", fg="white").grid(row=1, column=0, padx=10, pady=10)
        book_name_entry = tk.Entry(add_book_dialog)
        book_name_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(add_book_dialog, text="Enter Author Name:", bg="#16a167", fg="white").grid(row=2, column=0, padx=10, pady=10)
        author_entry = tk.Entry(add_book_dialog)
        author_entry.grid(row=2, column=1, padx=10, pady=10)

        def save_book():
            book_id = book_id_entry.get()
            book_name = book_name_entry.get()
            author = author_entry.get()

            if not book_id or not book_name or not author:
                messagebox.showwarning("Input Error", "All fields must be filled out.")
                return
            
            if not self.validate_book_id(book_id):
                messagebox.showerror("Error", "Invalid or duplicate Book ID.")
                return

            new_book = {"ID": book_id, "Name": book_name, "Author": author}
            self.books_data.append(new_book)
            
            # Check if authors_data is initialized and exists
            if not hasattr(self, 'authors_data'):
                print("Error: authors_data is not initialized.")
                self.authors_data = {}  # Initialize authors_data
     
            if author not in self.authors_data:
                self.authors_data[author] = [] # Update authors list
            
            self.authors_data[author].append(book_name)
            self.save_data()
            self.update_books_table()
            self.update_authors_table()
            messagebox.showinfo("Success", "Book added successfully.")
            add_book_dialog.destroy()

        tk.Button(add_book_dialog, text="Add Book", command=save_book, bg="#16a167", fg="white", relief="raised", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, pady=10)
    
    def validate_book_id(self, book_id):
        return all(book["ID"] != book_id for book in self.books_data)

    #---------------------------------------------------------------- Borrow book button ---------------------------------------------------------------------------

    def borrow_book(self):
        borrow_book_dialog = tk.Toplevel(self.root)
        borrow_book_dialog.title("Borrow Book")
        borrow_book_dialog.configure(bg="#16a167")

        tk.Label(borrow_book_dialog, text="Enter Book ID:", bg="#16a167", fg="white").grid(row=0, column=0, padx=10, pady=10)
        book_id_entry = tk.Entry(borrow_book_dialog)
        book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(borrow_book_dialog, text="Enter Borrower Name:", bg="#16a167", fg="white").grid(row=1, column=0, padx=10, pady=10)
        borrower_name_entry = tk.Entry(borrow_book_dialog)
        borrower_name_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(borrow_book_dialog, text="Enter Roll Number:", bg="#16a167", fg="white").grid(row=2, column=0, padx=10, pady=10)
        roll_number_entry = tk.Entry(borrow_book_dialog)
        roll_number_entry.grid(row=2, column=1, padx=10, pady=10)

        def submit_borrow():
            book_id = book_id_entry.get()
            borrower_name = borrower_name_entry.get()
            roll_number = roll_number_entry.get()
            
            book = next((b for b in self.books_data if b["ID"] == book_id), None)
            if book:
                borrowed_book = {
                    "Book ID": book["ID"],
                    "Book Name": book["Name"],
                    "Author": book["Author"],
                    "Borrower Name": borrower_name,
                    "Roll Number": roll_number
                }
                self.borrowers_data.append(borrowed_book)
                self.save_data()
                 # Check if borrowers_table is defined
                if hasattr(self, 'borrowers_table'):    
                    self.update_borrowers_table()
                else:
                    print("Error: borrowers_table not initialized //comment from add book section.")
                borrow_book_dialog.destroy()
            else:
                messagebox.showerror("Error", "Book ID not found.")

        tk.Button(borrow_book_dialog, text="Submit", command=submit_borrow, width=10, height=2, bg="#16a167", fg="white", relief="raised", font=("Arial", 12)).grid(row=3, columnspan=2, pady=10)
     

    #---------------------------------------------------------- Remove button logic ---------------------------------------------------------------------------------
    
    def remove_book(self):
        book_id = simpledialog.askstring("Remove Book", "Enter Book ID to remove:")
        # Find the book to remove
        book_to_remove = next((book for book in self.books_data if book["ID"] == book_id), None)
        
        if book_to_remove:
            # Remove the book from the books list
            self.books_data.remove(book_to_remove)
            # Remove the book from the authors' data
            author = book_to_remove["Author"]
            if author in self.authors_data:
                if book_to_remove["Name"] in self.authors_data[author]:
                    self.authors_data[author].remove(book_to_remove["Name"])
            
                # Remove the author if they have no more books
                if not self.authors_data[author]:
                    del self.authors_data[author]
        
            self.save_data()
            self.update_books_table()
            self.update_authors_table()
        else:
            messagebox.showerror("Error", "Book ID not found.")
 

    #--------------------------------------------------------------------- Authors Page ----------------------------------------------------------------------------------
    def show_authors(self):
        self.admin_frame.pack_forget()
        self.authors_frame = tk.Frame(self.root, bg="#990000")
        self.authors_frame.pack(fill='both', expand=True)

        # Create and grid the "Back button"
        # Define the buttons and their commands
        buttons = [
            ("Back", self.go_back_from_authors)
        ]
        
        row = 0
        col = 0
        for text, command in buttons:
            button = tk.Button(self.authors_frame, text=text, command=command, width=20, height=3, bg="#990000", relief="raised", font=("Arial", 12, "bold"))
            button.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            
        # Create and grid the authors table
        self.authors_table = ttk.Treeview(self.authors_frame, columns=("ID", "Name"), show='headings')
        self.authors_table.heading("ID", text="Author Name", anchor=tk.W)
        self.authors_table.heading("Name", text="Book Name", anchor=tk.W)
        self.authors_table.column("ID", width=100, anchor=tk.W)
        self.authors_table.column("Name", width=500, anchor=tk.W)
        self.authors_table.grid(row=row + 1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Adjust the row and column weights so the Treeview expands with the window
        self.authors_frame.grid_rowconfigure(row + 1, weight=1)
        self.authors_frame.grid_columnconfigure(0, weight=1)
        
        self.update_authors_table()
        
    def update_authors_table(self):
        
        if not hasattr(self, 'authors_table') or not self.authors_table.winfo_exists():
            return
          # Clear existing rows in the table
        for item in self.authors_table.get_children():
            self.authors_table.delete(item)
        
        self.load_data()
        if isinstance(self.authors_data, dict):               # Ensure self.authors_data is a dictionary
            sorted_authors = sorted(self.authors_data.keys()) # Sort authors by name in alphabetical order
            for author in sorted_authors:                     # Insert sorted author data into the table
                books_list = ", ".join(sorted(self.authors_data[author])) 
                self.authors_table.insert("", "end", values=(author, books_list))
            
    def go_back_from_authors(self):
        self.authors_frame.pack_forget()            #Navigation(shift authors frame to admin)
        self.create_admin_section()
        self.admin_frame.pack(pady=20)

    #---------------------------------------------------------------------- Borrowers page ---------------------------------------------------------------------------
    def show_borrowers(self):
        self.admin_frame.pack_forget()
        self.borrowers_frame = tk.Frame(self.root, bg="#433987")
        self.borrowers_frame.pack(pady=20)

        buttons = [
            ("Back", self.go_back_from_borrowers),
            ("Return Book", self.return_book)
        ]
        for i, (text, command) in enumerate(buttons):
            button = tk.Button(self.borrowers_frame, text=text, command=command, bg="#72a4fc", fg="white", relief="raised", bd=10, font=("Arial", 14, "bold"), width=20, height=2)
            button.grid(row=0, column=i, padx=30, pady=10)

        #create treeview for borrowers
        self.borrowers_table = ttk.Treeview(self.borrowers_frame, columns=("Roll Number", "Book Name", "Author", "Book ID", "Borrower Name"), show='headings')
        self.borrowers_table.heading("Roll Number", text="Roll Number", anchor=tk.W)
        self.borrowers_table.heading("Book Name", text="Book Name", anchor=tk.W)
        self.borrowers_table.heading("Author", text="Author", anchor=tk.W)
        self.borrowers_table.heading("Book ID", text="Book ID", anchor=tk.W)
        self.borrowers_table.heading("Borrower Name", text="Borrower Name", anchor=tk.W)
        self.borrowers_table.column("Roll Number", width=150, anchor=tk.W)
        self.borrowers_table.column("Book Name", width=300, anchor=tk.W)
        self.borrowers_table.column("Author", width=300, anchor=tk.W)
        self.borrowers_table.column("Book ID", width=100, anchor=tk.W)
        self.borrowers_table.column("Borrower Name", width=200, anchor=tk.W)

        # Use grid() for the Treeview
        self.borrowers_table.grid(row=1, column=0, columnspan=len(buttons), padx=10, pady=10, sticky="nsew")

        # Configure row and column weights to make the table expand
        self.borrowers_frame.grid_rowconfigure(1, weight=1)
        self.borrowers_frame.grid_columnconfigure(0, weight=1)

        self.update_borrowers_table()
   
    def update_borrowers_table(self):
        
        if not hasattr(self, 'borrowers_table') or not self.borrowers_table.winfo_exists():
            return                                       # Check if borrowers_table is initialized and exists
        
        for row in self.borrowers_table.get_children():  # Clear existing rows
            self.borrowers_table.delete(row)
        # Sort borrowers_data by "Roll Number" in ascending order
        sorted_borrowers = sorted(self.borrowers_data, key=lambda x: int(x["Roll Number"]))
    
         # Insert new rows
        for borrower in sorted_borrowers:         
            if all(key in borrower for key in ["Roll Number", "Book Name", "Author", "Book ID", "Borrower Name"]): # Ensure each borrower entry contains all required keys
                self.borrowers_table.insert("", tk.END, values=(
                    borrower["Roll Number"],
                    borrower["Book Name"],
                    borrower["Author"],
                    borrower["Book ID"],
                    borrower["Borrower Name"],
                ))
            else:
                print(f"Warning: Borrower data missing required fields: {borrower}")
        
    def go_back_from_borrowers(self):
        self.borrowers_frame.pack_forget()  # Navigation (shift frame borrow to admin section)
        self.create_admin_section()
        self.admin_frame.pack(pady=20)
        
    def return_book(self):  # --------------------------------- Return book button (from author page)--------------------------------------------
        # Create the return book dialogzz
        dialog = tk.Toplevel(self.root)
        dialog.title("Return Book")

        tk.Label(dialog, text="Roll Number").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(dialog, text="Book ID").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(dialog, text="Student Name").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(dialog, text="Late (in days)").grid(row=3, column=0, padx=10, pady=5)

        roll_number_entry = tk.Entry(dialog)
        book_id_entry = tk.Entry(dialog)
        student_name_entry = tk.Entry(dialog)            
        late_days_entry = tk.Entry(dialog)

        book_id_entry.grid(row=1, column=1, padx=10, pady=5)
        roll_number_entry.grid(row=0, column=1, padx=10, pady=5)
        student_name_entry.grid(row=2, column=1, padx=10, pady=5)
        late_days_entry.grid(row=3, column=1, padx=10, pady=5)

        def submit():
            book_id = book_id_entry.get()
            roll_number = roll_number_entry.get()
            student_name = student_name_entry.get()
            try:
                late_days = int(late_days_entry.get())
                if late_days < 0:
                    messagebox.showerror("Error", "Late days cannot be negative.")
                    return                 # Exit if the late days are negative
            except ValueError:
                messagebox.showerror("Error", "Invalid number of late days.")
                return              # Exit if the late days input is not a valid intege

            # Calculate the fine
            fine_amount = late_days * 1  # Assuming 1 Rs per day


            # Match and remove the book entry from the borrowers list
            matched_borrower = next((borrower for borrower in self.borrowers_data 
                                     if borrower["Book ID"] == book_id and borrower["Roll Number"] == roll_number), None)
            if matched_borrower:
                self.borrowers_data = [borrower for borrower in self.borrowers_data 
                                       if not (borrower["Book ID"] == book_id and borrower["Roll Number"] == roll_number)]
                self.save_data()
                self.update_borrowers_table()
                
                 # Show the confirmation dialog before going to the due section
                confirmation_dialog = tk.Toplevel(self.root)
                confirmation_dialog.title("Note the details")

                message = f"{student_name}- roll num. {roll_number}, has a Due amount of {fine_amount:.2f}."
                tk.Label(confirmation_dialog, text=message, padx=10, pady=10).pack()
                
                def go_to_due():
                    confirmation_dialog.destroy()
                    self.show_due()  # Go to the due section
                tk.Button(confirmation_dialog, text="Go to Due", command=go_to_due, padx=10, pady=5).pack()
                dialog.destroy()
   
            else:
                messagebox.showerror("Error", "Book not found with this roll number.")

        tk.Button(dialog, text="Submit", command=submit).grid(row=4, column=0, columnspan=2, pady=10)

            
            
    
   #---------------------------------------------------------------------- Due section ---------------------------------------------------------------------------
    
    def show_due(self):
        # Clear the current content
        for widget in self.root.winfo_children():
            widget.destroy()
    
        
        self.due_frame = tk.Frame(self.root, bg="#433987")
        self.due_frame.pack(pady=10, fill=tk.BOTH, expand=True)
     
        tk.Label(self.due_frame, text="Due Section", bg="#433987", fg="white", font=("Arial", 20)).grid(row=0, column=0, columnspan=3, pady=10)

        # Create a frame for the books table and place it in the next row
        due_table_frame = tk.Frame(self.due_frame, bg="#433987")
        due_table_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky='nsew')

        self.due_table = ttk.Treeview(due_table_frame, columns=("ID", "Name", "Author"), show='headings')
        self.due_table.heading("ID", text="Student Roll Number", anchor=tk.W)
        self.due_table.heading("Name", text="Student Name", anchor=tk.W)
        self.due_table.heading("Author", text="Due/Fine Amount", anchor=tk.W)
        self.due_table.column("ID", width=100, anchor=tk.W)
        self.due_table.column("Name", width=400, anchor=tk.W)
        self.due_table.column("Author", width=300, anchor=tk.W)
        self.due_table.grid(row=0, column=0, sticky='nsew')
        
        # Configure the grid to ensure the books table expands
        self.due_frame.grid_rowconfigure(2, weight=1)
        self.due_frame.grid_columnconfigure(0, weight=1)
        due_table_frame.grid_rowconfigure(0, weight=1)
        due_table_frame.grid_columnconfigure(0, weight=1)
              
        self.load_due_data()
        self.display_due_data()

        self.create_buttons()
        # Create a back button
        back_button = tk.Button(self.due_frame, text="Back", command=self.go_back_from_dues, width=20, height=2, bg="#c2d9f2", relief="raised", font=("Arial", 12))
        back_button.grid(row=4, column=0, columnspan=3, pady=10, sticky='s')
        
    def display_due_data(self):
        # Clear existing data in the table
        for item in self.due_table.get_children():
            self.due_table.delete(item)
            
        # Insert due data into the table
        for due in self.due_data:
            self.due_table.insert("", "end", values=(due['id'], due['name'], due['amount']))
        
    def create_buttons(self):
        buttons_frame = tk.Frame(self.due_frame, bg="#433987")
        buttons_frame.grid(row=3, column=0, columnspan=3, pady=10, sticky='ew')

        add_due_button = tk.Button(buttons_frame, text="Add Due", command=self.add_due, width=15, height=2, bg="#c2d9f2", relief="raised", font=("Arial", 12))
        add_due_button.grid(row=0, column=0, padx=5)

        pay_due_button = tk.Button(buttons_frame, text="Pay Due", command=self.pay_due, width=15, height=2, bg="#c2d9f2", relief="raised", font=("Arial", 12))
        pay_due_button.grid(row=0, column=1, padx=5)

        add_student_button = tk.Button(buttons_frame, text="Add Student", command=self.add_student, width=15, height=2, bg="#c2d9f2", relief="raised", font=("Arial", 12))
        add_student_button.grid(row=0, column=2, padx=5)

        remove_student_button = tk.Button(buttons_frame, text="Remove Student", command=self.remove_student, width=15, height=2, bg="#c2d9f2", relief="raised", font=("Arial", 12))
        remove_student_button.grid(row=0, column=3, padx=5)

    def load_due_data(self):
        try:
            with open('dues.json', 'r') as file:
                self.due_data = json.load(file)
        except FileNotFoundError:
            self.due_data = []  # Initialize with empty list if file is not found
        except json.JSONDecodeError:
            print("Error decoding JSON from dues.json. Initializing empty due data.")
            self.due_data = [] 

    def add_due(self): #--------------------------------- Add due button --------------------------------------------------------------------
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Due")

        tk.Label(dialog, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(dialog, text="Student Name").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(dialog, text="Due Amount").grid(row=2, column=0, padx=10, pady=5)

        id_entry = tk.Entry(dialog)
        name_entry = tk.Entry(dialog)
        amount_entry = tk.Entry(dialog)                             

        id_entry.grid(row=0, column=1, padx=10, pady=5)
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        amount_entry.grid(row=2, column=1, padx=10, pady=5)
        
        def submit():
            student_id = id_entry.get()
            student_name = name_entry.get()
            try:
                due_amount = float(amount_entry.get())
                if due_amount < 0:
                    messagebox.showerror("Error", "Due amount must be 0 or a positive number.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid amount.")
                return

            # Check if student ID exists
            existing_due = next((d for d in self.due_data if d['id'] == student_id), None)
            if existing_due:
                # Update due amount if student ID exists
                existing_due['amount'] = str(float(existing_due['amount']) + due_amount)
            else:
                # Add new student
                self.due_data.append({'id': student_id, 'name': student_name, 'amount': str(due_amount)})

            self.save_due_data()
            self.update_due_list()
            self.load_due_data()
            dialog.destroy()

        tk.Button(dialog, text="Submit", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

    def pay_due(self): #----------------------------------------Pay Due Button-------------------------------------------------------------------
        dialog = tk.Toplevel(self.root)
        dialog.title("Pay Due")

        tk.Label(dialog, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(dialog, text="Pay Amount").grid(row=1, column=0, padx=10, pady=5)

        id_entry = tk.Entry(dialog)
        amount_entry = tk.Entry(dialog)

        id_entry.grid(row=0, column=1, padx=10, pady=5)            
        amount_entry.grid(row=1, column=1, padx=10, pady=5)

        def submit():
            student_id = id_entry.get()
            try:
                pay_amount = float(amount_entry.get())
                if pay_amount <= 0:
                    messagebox.showerror("Error", "Pay amount must be a positive number.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid amount.")
                return

            due_entry = next((d for d in self.due_data if d['id'] == student_id), None)
            if due_entry:
                due_amount = float(due_entry['amount'])
                new_amount = due_amount - pay_amount
                if new_amount < 0:
                    messagebox.showinfo("Info", f"Return amount: {new_amount:.2f}")
                if new_amount <= 0:
                    self.due_data = [d for d in self.due_data if d['id'] != student_id]
                else:
                    due_entry['amount'] = str(new_amount)
                self.save_due_data()
                self.update_due_list()
                self.load_due_data()
            else:
                messagebox.showerror("Error", "Student ID not found.")
            dialog.destroy()

        tk.Button(dialog, text="Submit", command=submit).grid(row=2, column=0, columnspan=2, pady=10)

    def add_student(self): #------------------------------------------ Add student Button ---------------------------------------------------------------
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Student")

        tk.Label(dialog, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(dialog, text="Student Name").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(dialog, text="Due Amount").grid(row=2, column=0, padx=10, pady=5)

        id_entry = tk.Entry(dialog)
        name_entry = tk.Entry(dialog)
        amount_entry = tk.Entry(dialog)

        id_entry.grid(row=0, column=1, padx=10, pady=5)
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        amount_entry.grid(row=2, column=1, padx=10, pady=5)

        def submit():
            student_id = id_entry.get()                                        
            student_name = name_entry.get()
            try:
                due_amount = float(amount_entry.get())
                if due_amount < 0:
                    messagebox.showerror("Error", "Due amount must be 0 or a positive number.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid amount.")
                return

            # Check if student ID exists
            existing_due = next((d for d in self.due_data if d['id'] == student_id), None)
            if existing_due:
                messagebox.showerror("Error", "Student ID already exists.")
            else:
                # Add new student
                self.due_data.append({'id': student_id, 'name': student_name, 'amount': str(due_amount)})
                self.save_due_data()
                self.update_due_list()
                self.load_due_data()
                dialog.destroy()

        tk.Button(dialog, text="Submit", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

    def remove_student(self): #---------------------------------- Remove student button -------------------------------------------------------------------
        dialog = tk.Toplevel(self.root)
        dialog.title("Remove Student")

        tk.Label(dialog, text="Student ID").grid(row=0, column=0, padx=10, pady=5)

        id_entry = tk.Entry(dialog)                             
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        def submit():
            student_id = id_entry.get()
            due_entry = next((d for d in self.due_data if d['id'] == student_id), None)
            if due_entry:
                due_amount = float(due_entry['amount'])
                if due_amount > 0:
                    result = messagebox.askyesno("Confirm", f"Student ID: {student_id}\nDue Amount: {due_amount:.2f}\nDo you want to mark it as ' Due Paid'?")
                    if result:
                        self.due_data = [d for d in self.due_data if d['id'] != student_id]
                        self.save_due_data()
                        self.update_due_list()
                        self.load_due_data()
                else:
                   # Display negative amount as a message
                    messagebox.showinfo("Info", f"Remaining due amount after removal: {due_amount:.2f}")
                    self.due_data = [d for d in self.due_data if d['id'] != student_id]
                    self.save_due_data()
                    self.update_due_list()
            else:
                messagebox.showerror("Error", "Student ID not found.")
            dialog.destroy()

        tk.Button(dialog, text="Submit", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

    def update_due_list(self):
        # Clear existing data in the table
        for item in self.due_table.get_children():
            self.due_table.delete(item)
    
        # Insert updated due data into the table
        for due in self.due_data:
            self.due_table.insert("", "end", values=(due['id'], due['name'], due['amount']))


    def save_due_data(self):
        with open('dues.json', 'w') as file:
            json.dump(self.due_data, file, indent=4)

    def go_back_from_dues(self):
        self.due_frame.pack_forget()
        self.create_admin_section() # Navigation (From Due section to admin frame)
        self.admin_frame.pack(pady=20)

 
    #------------------------------------------------------------------ Here is User page UI ----------------------------------------------------------------------
    
    def create_user_section(self):
        self.user_frame = tk.Frame(self.root, bg="#433987")
        self.user_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        tk.Label(self.user_frame, text="Welcome to the Library", bg="#433987", fg="white", font=("Arial", 20)).grid(row=0, column=0, columnspan=3, pady=10)
         # Create a frame for the buttons and pack it
        button_frame = tk.Frame(self.user_frame, bg="#433987")
        button_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky='ew')
        
        tk.Button(button_frame, text="Back", command=self.go_back_from_user, width=20, height=3, bg="#c2d9f2", relief="raised", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Digital Library", command=self.open_digital_library, width=20, height=3, bg="#ffbf00", relief="raised", font=("Arial", 12)).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Online Courses\n SWAYAM", command=self.open_online_courses, width=20, height=3, bg="#00bfff", relief="raised", font=("Arial", 12)).grid(row=0, column=2, padx=5)

        # Create a frame for the books table and place it in the next row
        books_table_frame = tk.Frame(self.user_frame, bg="#433987")
        books_table_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky='nsew')

        self.books_table = ttk.Treeview(books_table_frame, columns=("ID", "Name", "Author"), show='headings')
        self.books_table.heading("ID", text="ID", anchor=tk.W)
        self.books_table.heading("Name", text="Book Name", anchor=tk.W)
        self.books_table.heading("Author", text="Author", anchor=tk.W)
        self.books_table.column("ID", width=100, anchor=tk.W)
        self.books_table.column("Name", width=400, anchor=tk.W)
        self.books_table.column("Author", width=300, anchor=tk.W)
        self.books_table.grid(row=0, column=0, sticky='nsew')
        
        # Configure the grid to ensure the books table expands
        self.user_frame.grid_rowconfigure(2, weight=1)
        self.user_frame.grid_columnconfigure(1, weight=0)
        self.user_frame.grid_columnconfigure(0, weight=1)
        self.user_frame.grid_columnconfigure(1, weight=1)
        books_table_frame.grid_rowconfigure(0, weight=1)
        books_table_frame.grid_columnconfigure(0, weight=1)

        self.update_books_table()
        
    def open_digital_library(self):
        url = "https://ndl.iitkgp.ac.in/"  
        webbrowser.open(url, new=2) 
    
    def open_online_courses(self):
        url = "https://swayam.gov.in/explorer"  
        webbrowser.open(url, new=2) 
        
    def go_back_from_user(self):
        self.user_frame.pack_forget()       # Navigation(shift user frame to welcome frame"starting")
        self.create_welcome_widgets()
        self.welcome_frame.pack(pady=20)
         
    # ----------------------------------------------------------------- save data / load data / load books-------------------------------------------------------------------------------------
        
    def save_data(self):
         try:
            with open(BOOKS_FILE, "w") as f:
                json.dump(self.books_data, f, indent=4)
            with open(AUTHORS_FILE, "w") as f:
                json.dump(self.authors_data, f, indent=4)           #saving data to json-file
            with open(BORROWERS_FILE, "w") as f:
                json.dump(self.borrowers_data, f, indent=4)
            with open(DUES_FILE, "w") as f:
                json.dump(self.due_data, f, indent=4)
         except IOError as e:
            print(f"An error occurred while saving data: {e}")
         
    def load_books():
        try:
            with open("books.json", "r") as f:              #load books datasheet
                return json.load(f)
        except FileNotFoundError:
            return []
        
    def load_data(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "r") as f:
                self.books_data = json.load(f)                  #load all/any data from json files
        else:
            self.books_data = []
            
        if os.path.exists(AUTHORS_FILE):
            with open(AUTHORS_FILE, "r") as f:
                self.authors_data = json.load(f)
        else:
            self.authors_data = {}
            
        if os.path.exists(BORROWERS_FILE):
            with open(BORROWERS_FILE, "r") as f:
                self.borrowers_data = json.load(f)
        else:
            self.borrowers_data = []
        
        if os.path.exists(DUES_FILE):
            with open(DUES_FILE, "r") as f:
                self.due_data = json.load(f)
        else:
            self.due_data = []
            
    def load_json(self, filename):
        path = resource_path(filename)
        print(f"Loading JSON from: {path}")  # Debug print check for successfull initialization process
        try:
            with open(path, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return {}
#--------------------------------------------------------------------End of the logic!.....;p -------------------------------------------------------------------------------            

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
