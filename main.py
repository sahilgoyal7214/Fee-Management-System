import os
import MySQLdb as c
import numpy

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
                                                                                                --Abhishek Rajput,XII-A
                                                                                                
                                                                                                Guided by :-
                                                                                                -- MR.Ashok Kumar Rao Sir




                                               WELCOME TO FEES MANAGEMENT SYSTEM

''')

def backup_database(db_name):
    """Create a backup of the database."""
    try:
        # Construct the mysqldump command to create a backup
        backup_file = f"{db_name}_backup.sql"
        os.system(f"mysqldump -u root -pAnsh@2521 {db_name} > {backup_file}")
        print(f"Backup successful! Database {db_name} backed up to {backup_file}")
    except Exception as e:
        print(f"Error during backup: {e}")

def restore_database(db_name, backup_file):
    """Restore the database from a backup file."""
    try:
        # Construct the mysql command to restore the backup
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cursor.execute(f"CREATE DATABASE {db_name}")
        os.system(f"mysql -u root -pAnsh@2521 {db_name} < {backup_file}")
        print(f"Restore successful! Database {db_name} restored from {backup_file}")
    except Exception as e:
        print(f"Error during restore: {e}")

def Main():
    print()
    
    x = int(input('''                                                           MAIN MENU

Enter 0 to Show All Fees Databases 
Enter 1 for Fees Database Creation
Enter 2 for Table Creation
Enter 3 for Fees Database Deletion
Enter 4 for Table Deletion
Enter 5 for Students Data Entry in Table
Enter 6 for Students Data Deletion from Table
Enter 7 for Backup Database
Enter 8 for Restore Database
Enter 9 to Stop
Enter Choice:\n
'''))

    if x == 0:
        Database_show()
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
        db_name = input("Enter the name of the database to backup: ")
        backup_database(db_name)
    elif x == 8:
        db_name = input("Enter the name of the database to restore: ")
        backup_file = input("Enter the backup file name (e.g., database_backup.sql): ")
        restore_database(db_name, backup_file)
    elif x == 9:
        print("                                                           THANKS")
    else:
        print("Enter Correct value!")
        Main()

def Database_show():
    print("Fees Databases are:\n")
    cursor.execute("show databases")
    for i in cursor:
        print(i[0])
    print()

def New_Database():
    print("                                                     FEES DATABASE CREATION MENU\n")
    Database_show()
    print("Fees Database Creation\n")
    a = input("Enter Name of the New Fees Database: ")
    cursor.execute(f"create database {a}")
    print(f"Fees Database '{a}' Created\n")
    Database_show()

def Table():
    print("                                                       TABLE CREATION MENU\n")
    Database_show()
    c = input("Enter name of the Fees Database in which you want to create table: ")
    cursor.execute(f"use {c}")
    d = input("Enter Name of new Table: ")
    e = input("Enter Row Heading with specified data type (e.g., rollno int, name char(50), fees decimal(6,2)): ")
    cursor.execute(f"create table {d} ({e})")
    print("Table Created Successfully\n")

def Database_Del():
    print("                                                  FEES DATABASE DELETION MENU\n")
    Database_show()
    g = input("Enter Fees Database name which you want to Delete: ")
    cursor.execute(f"drop database {g}")
    print(f"Fees Database '{g}' Deleted Successfully\n")

def Table_Del():
    print("                                                      TABLE DELETION MENU\n")
    Database_show()
    new = input("Enter Fees Database name in which you want to Delete the Table: ")
    cursor.execute(f"use {new}")
    new1 = input("Enter Table name which you want to Delete: ")
    cursor.execute(f"drop table {new1}")
    print(f"Table '{new1}' Deleted Successfully\n")

def Data_Entry():
    print("                                                     STUDENT DATA ENTRY MENU\n")
    Database_show()
    h = input("Enter Fees Database: ")
    cursor.execute(f"use {h}")
    k = input("Enter Table: ")
    m = input("Enter Student Data (e.g., (1,'Abhi',300)): ")
    cursor.execute(f"Insert into {k} values {m}")
    print("Student Data Inserted Successfully\n")

def Data_Del():
    print("                                                    STUDENT DATA DELETION MENU\n")
    Database_show()
    n = input("Enter Fees Database: ")
    cursor.execute(f"use {n}")
    o = input("Enter Table: ")
    p = input(f"Enter ID to delete: ")
    cursor.execute(f"delete from {o} where id = {p}")
    print("Student Data Deleted Successfully\n")

Main()
