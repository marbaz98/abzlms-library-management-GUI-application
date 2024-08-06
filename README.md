
# Library Management System

This project is a GUI-based Library Management System implemented using Python and Tkinter. It provides functionalities for managing books, authors, borrowers, and dues. The application uses JSON files for data persistence, making it easy to store and retrieve data without requiring external database software.

## Features

- **Admin Section**:
  - View and manage borrowers' names, issue dates, book names, and dues.
  - Create new users and passwords.
  - View any user's password.
- **User Section**:
  - View author names, book names, issue dates, and due amounts.
- **Book Management**:
  - Add new books.
  - View available books in a table format.
  - Borrow books and register them to borrowers.
  - Return books.
  - Remove books and update the author's list accordingly.
- **Author Management**:
  - View all author entries in a table format.
  - Manage books associated with authors.
- **Due Management**:
  - Display a list of dues with student names and their dues amounts.
  - Due amounts are displayed in either red or green.
- **General**:
  - Use of Tkinter `tk.Toplevel` dialogs for data entry.
  - Consistent use of Tkinter geometry managers (`pack`, `grid`) to avoid layout issues.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Pillow

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/md-arbaz98/abzlms.git
   cd abzlms
   ```

2. Ensure that you have Python installed. If not, download and install it from [python.org](https://www.python.org/).

3. Install required dependencies:
   ```bash
   pip install tk
   pip install pillow
   ```

## Usage

1. Run the application:
   ```bash
   python arbazLMS.py
   ```

2. Use the admin credentials to log in:
   - **Username**: `admin`
   - **Password**: `password`

3. Navigate through different sections using the buttons provided.

## File Structure

- `arbazLMS.py`: Main application file.
- `books.json`: JSON file to store book data.
- `authors.json`: JSON file to store author data.
- `borrowers.json`: JSON file to store borrower data.
- `dues.json`: JSON file to store due data.

## Data Persistence

The application uses JSON files for storing data, which are:
- `books.json`: Contains information about books.
- `authors.json`: Contains information about authors.
- `borrowers.json`: Contains information about borrowers.
- `dues.json`: Contains information about dues.

## Screenshots

## Contribution

Feel free to fork this repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

**
