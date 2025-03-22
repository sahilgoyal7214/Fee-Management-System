import MySQLdb as c
import sys
import os

mydb = c.connect(
    host="localhost",
    user="root",
    passwd="Ansh@2521",
    charset="utf8"
)

cursor = mydb.cursor() #cursor

print('''
-------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------
 |||||| |||||| |||||| ||||||    ||     ||     |     ||    ||     |     |||||||| |||||| ||     || |||||| ||    || ||||||
 ||     ||     ||     ||        || | | ||    | |    ||||  ||    | |    ||       ||     || | | || ||     ||||  ||   ||
 ||||   ||||   ||||   ||||||    ||  |  ||   |||||   || || ||   |||||   || ||||| ||||   ||  |  || ||||   || || ||   ||
 ||     ||     ||         ||    ||     ||  ||   ||  ||  ||||  ||   ||  || || || ||     ||     || ||     ||  ||||   ||
 ||     |||||| |||||| ||||||    ||     || ||     || ||    || ||     || ||||| || |||||| ||     || |||||| ||    ||   ||
-------------------------------------------------------------------------------------------------------------------------    
-------------------------------------------------------------------------------------------------------------------------

                                                                                                Prepared by :-
                                                                                                --Sahil Goyal,AIML-B
                                                                                                
                                                                                                Guided by :-
                                                                                                -- MR.Ashok Kumar Rao Sir
                                                                                                
                                                                                                Collaborators:
                                                                                                --Ansh Sharma
                                                                                                --Akhsaj Chainani
                                                                                                --Karv Amin


                                               WELCOME TO FEES MANAGEMENT SYSTEM

''')


def Main():
    while True:  # Loop to repeatedly show the main menu
        print()
        try:
            x = int(input('''                                                           MAIN MENU

Enter 0 to Show All Fees Databases 
Enter 1 for Fees Database Creation
Enter 2 for Table Creation
Enter 3 for Fees Database Deletion
Enter 4 for Table Deletion
Enter 5 for Students Data Entry in Table
Enter 6 for Students Data Deletion from Table
Enter 7 to Backup Database
Enter 8 to Restore Database
Enter 9 to stop
Enter Choice:\n
'''))

            if x == 0:
                show_all_fees_databases()
            elif x == 1:
                New_Database()
            elif x == 2:
                Table()
            elif x == 3:
                Database_Del()
            elif x == 4:
                Table_Del()
            elif x == 5:
                Data_Entry()
            elif x == 6:
                Data_Del()
            elif x == 7:
                Backup_Database()
            elif x == 8:
                Restore_Database()
            elif x == 9:
                print("                                                           THANKS")
                break  # Exit the loop and stop the program
            else:
                print("Enter a valid number from 0 to 9!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def show_all_fees_databases():
    while True:
        print("                                                         DATABASE MENU\n")
        Database_show()
        z = input("Enter Fees Database name if you want to show content of any database or 1 to go to Main Menu: ")
        if z == "":
            print("Enter Something")
            continue
        elif z == "1":
            break  # Go back to Main Menu
        else:
            cursor.execute(f"USE {z}")
            cursor.execute("SHOW TABLES")
            lst = cursor.fetchall()
            print("Tables =\n", lst)

            if lst:
                w = input("Enter Name of the Table: ")
                if w == "":
                    print("Enter Something")
                    continue

                print("Heading Row in Selected Table: \n")
                cursor.execute(f"SHOW COLUMNS FROM {w}")
                for i in cursor:
                    print(i[0], end=" | ")
                print()

                print("Student Data in Selected Table: \n")
                cursor.execute(f"SELECT * FROM {w}")
                for i in cursor:
                    print(i)
                print()
            else:
                print("No Table Found\n")
                continue

            try:
                y = int(input("Enter 0 to show all Fees databases or 1 to go to Main Menu: "))
                if y == 1:
                    break
            except ValueError:
                print("Invalid input! Going back to the Main Menu.")
                break


def Database_show():
    print("Fees Databases are:\n")
    cursor.execute("SHOW DATABASES")
    for i in cursor:
        print(i[0])
    print()


def New_Database():
    while True:
        print("                                                     FEES DATABASE CREATION MENU\n")
        Database_show()
        print("Fees Database Creation\n")

        a = input("Enter Name of the New Fees Database \nDo not use names which are already present in Fees Database list:\n")
        cursor.execute(f"CREATE DATABASE {a}")
        print("Fees Database Created\n")
        Database_show()

        try:
            b = int(input("Enter 0 to do Table Creation in New Fees Database or 1 to go to Main Menu: "))
            if b == 0:
                Table()
            else:
                break
        except ValueError:
            print("Invalid input! Returning to the Main Menu.")
            break

        try:
            k = int(input("Enter 0 to create new Fees database or 1 to stop: "))
            if k == 1:
                break
        except ValueError:
            print("Invalid input! Stopping database creation.")
            break


def Table():
    print("                                                       TABLE CREATION MENU\n")
    while True:
        Database_show()
        c = input("Enter name of the Fees Database in which you want to create table: ")
        cursor.execute(f"USE {c}")
        cursor.execute("SHOW TABLES")
        lst = cursor.fetchall()
        print("Tables =\n", lst)

        d = input("Enter Name of new Table= ")
        e = input('''Enter Row Heading with specified data type (Ex:rollno int,name char(50),fees decimal(6,2)) to add in the Table :
Note: Do not use special characters like full stops, etc., and do not use spaces between Row Headings! \n''')
        cursor.execute(f"CREATE TABLE {d}({e})")
        print("Heading Row Created Successfully\n")

        try:
            f = int(input("Enter 0 to do Student Data Entry in New Fees Database or 1 to go to Main Menu: "))
            if f == 0:
                Data_Entry()
            else:
                break
        except ValueError:
            print("Invalid input! Returning to the Main Menu.")
            break


def Database_Del():
    print("                                                  FEES DATABASE DELETION MENU\n")
    while True:
        Database_show()
        g = input("Enter Fees Database name which you want to Delete: ")
        cursor.execute(f"DROP DATABASE {g}")
        print("Fees Database Deleted Successfully\n")
        Database_show()

        try:
            k = int(input("Enter 0 to delete more fees databases or 1 to stop: "))
            if k == 1:
                break
        except ValueError:
            print("Invalid input! Stopping database deletion.")
            break


def Table_Del():
    print("                                                      TABLE DELETION MENU\n")
    while True:
        Database_show()
        new = input("Enter Fees Database name in which you want to Delete the Table: ")
        cursor.execute(f"USE {new}")
        cursor.execute("SHOW TABLES")
        lst = cursor.fetchall()
        print("Tables =\n", lst)

        new1 = input("Enter Table name which you want to Delete: ")
        cursor.execute(f"DROP TABLE {new1}")
        print("Table Deleted Successfully\n")

        try:
            k = int(input("Enter 0 to delete more tables or 1 to stop: "))
            if k == 1:
                break
        except ValueError:
            print("Invalid input! Stopping table deletion.")
            break


def Data_Entry():
    print("                                                     STUDENT DATA ENTRY MENU\n")
    while True:
        Database_show()
        h = input("Enter Fees Database: ")
        cursor.execute(f"USE {h}")
        cursor.execute("SHOW TABLES")
        lst = cursor.fetchall()
        print("Tables =\n", lst)

        if len(lst) > 0:
            k = input("Enter Table: ")
            cursor.execute(f"SHOW COLUMNS FROM {k}")
            print("Heading Row in Selected Database: \n")
            for i in cursor:
                print(i[0], end=" | ")
            print()

            m = input(f'''Enter Student Data as in sequence with Heading Rows
Note: Apply round brackets at starting and ending of entry
      Use inverted commas for data in heading rows with varchar value
      Don't use special characters: ''')
            cursor.execute(f"INSERT INTO {k} VALUES{m}")
            print("Student Data Inserted Successfully\n")

            try:
                y = int(input("Enter 0 to insert more Student Data or 1 to stop: "))
                if y == 1:
                    break
            except ValueError:
                print("Invalid input! Stopping data entry.")
                break
        else:
            print("No tables found in the database.")


def Data_Del():
    print("                                                     STUDENT DATA DELETION MENU\n")
    while True:
        Database_show()
        i = input("Enter Fees Database name: ")
        cursor.execute(f"USE {i}")
        cursor.execute("SHOW TABLES")
        lst = cursor.fetchall()
        print("Tables =\n", lst)

        j = input("Enter Table name: ")
        cursor.execute(f"SHOW COLUMNS FROM {j}")
        print("Heading Row in Selected Database: \n")
        for i in cursor:
            print(i[0], end=" | ")
        print()

        n = input(f"Enter student roll number to delete: ")
        cursor.execute(f"DELETE FROM {j} WHERE rollno={n}")
        print("Student Data Deleted Successfully\n")

        try:
            y = int(input("Enter 0 to delete more Student Data or 1 to stop: "))
            if y == 1:
                break
        except ValueError:
            print("Invalid input! Stopping data deletion.")
            break


def Backup_Database():
    print("                                                     BACKUP DATABASE MENU\n")
    dbname = input("Enter the name of the database to backup: ")
    backup_file = f"{dbname}_backup.sql"
    os.system(f"mysqldump -u root -p {dbname} > {backup_file}")
    print(f"Backup of database '{dbname}' completed successfully into '{backup_file}'")


def Restore_Database():
    print("                                                     RESTORE DATABASE MENU\n")
    dbname = input("Enter the name of the database to restore: ")
    backup_file = f"{dbname}_backup.sql"
    os.system(f"mysql -u root -p {dbname} < {backup_file}")
    print(f"Database '{dbname}' restored successfully from '{backup_file}'")


Main()
