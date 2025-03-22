# Fee Management System

A **command-line based Fee Management System** built in Python to help educational institutions manage student fee data efficiently. This system interacts with a MySQL database and provides a menu-driven interface for creating fee databases, tables, inserting/deleting student records, and managing database backups/restores.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Credits](#credits)

---

## Overview

The **Fee Management System** is designed to simplify the administration of fee records. With a straightforward, text-based interface, it allows administrators to:

- Create new fee databases and tables.
- Insert and delete student fee data.
- Backup and restore fee databases.
- Delete databases and tables as needed.

This tool is particularly useful for institutions that need a lightweight and interactive system for fee management without the overhead of a full web application.

---

## Features

- **Database Operations:**  
  - List all available fee databases.
  - Create new fee databases.
  - Delete existing fee databases.

- **Table Operations:**  
  - Create new tables with custom column definitions.
  - Delete existing tables from a database.
  - Display table headings and data.

- **Data Management:**  
  - Insert student data into fee tables.
  - Delete specific student records (using roll numbers).

- **Backup & Restore:**  
  - Backup a fee database using `mysqldump`.
  - Restore a fee database from a backup file.

- **Interactive Menu:**  
  - Provides a user-friendly main menu to navigate various operations.
  - Error handling for invalid inputs.

- **Custom ASCII Banner:**  
  - Displays an ASCII art banner with credits and welcome message on startup.

---

## Technologies Used

- **Programming Language:** Python  
- **Database:** MySQL  
- **Python Library:** MySQLdb (for database connectivity)  
- **OS Integration:** Uses system calls for backup and restore operations

---

## Prerequisites

- **Python 3.8+**  
- **MySQL Server** installed and running locally  
- **MySQLdb (mysqlclient)** Python package  
  - Install via pip if not already installed:
    ```bash
    pip install mysqlclient
    ```
- Proper configuration of MySQL credentials in the script (in `main.py`):
  - Host, user, password, and charset are defined at the start of the file.

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sahilgoyal7214/Fee-Management-System.git
   cd Fee-Management-System
   ```

2. **Install Dependencies:**
   Ensure that you have the required Python packages. If you are using a virtual environment, activate it and then run:
   ```bash
   pip install mysqlclient
   ```

3. **Configure MySQL Connection:**
   - Open `main.py` and update the MySQL connection parameters if needed:
     ```python
     mydb = c.connect(
         host="localhost",
         user="root",
         passwd="YourMySQLPassword",
         charset="utf8"
     )
     ```

---

## Usage

1. **Run the Application:**
   ```bash
   python main.py
   ```
2. **Follow the Interactive Menu:**
   - The program displays a welcome banner along with the main menu.
   - Input a number from 0 to 9 to perform tasks such as:
     - Viewing available fee databases.
     - Creating or deleting databases and tables.
     - Inserting or deleting student fee records.
     - Backing up or restoring a database.
   - Enter valid inputs as prompted to navigate the system.
3. **Exiting:**
   - Choose the option to stop (enter 9) from the main menu when finished.

---

## Project Structure

```
Fee-Management-System/
│
├── main.py             # Main Python script containing the application logic
├── README.md           # Project documentation (this file)
```

---

## Contributing

Contributions to improve this Fee Management System are welcome! To contribute:

1. **Fork the Repository**
2. **Create a New Branch:**
   ```bash
   git checkout -b feature-branch-name
   ```
3. **Commit Your Changes:**
   ```bash
   git commit -m "Description of your changes"
   ```
4. **Push to Your Branch:**
   ```bash
   git push origin feature-branch-name
   ```
5. **Open a Pull Request** on GitHub.

---

## Credits

- **Prepared by:** [Sahil Goyal](https://github.com/sahilgoyal7214)  
- **Guided by:** Mr. Ashok Kumar Rao Sir  
- **Collaborators:**  
  - [Ansh Sharma](https://github.com/AnshSharma2521)  
  - [Akhsaj Chainani](https://github.com/akshajchainani)  
  - Karv Amin

---
