def Main():
    print()
    
    x=int(input('''                                                           MAIN MENU

Enter 0 to Show All Fees Databases 
Enter 1 for Fees Database Creation
Enter 2 for Table Creation
Enter 3 for Fees Database Deletion
Enter 4 for Table Deletion
Enter 5 for Students Data Entry in Table
Enter 6 for Students Data Deletion from Table
Enter 7 to stop
Enter Choice:\n
'''))

    if x==0:
        y=0
        while y==0:
            print("                                                         DATABASE MENU\n")
            Database_show()
            z=input("Enter Fees Database name if you want to show content of any database or 1 to go to Main Menu: ")
            print()
            if z=="":
                print("Enter Something")
                continue
            elif z=="1":
                Main()
                break
            else:
                cursor.execute("use {}".format(z))
                cursor.execute("show tables")
                lst=cursor.fetchall()
                print("Tables =\n")
                print(lst)
                print()

                if len(lst)>0:
                    w=input("Enter Name of the Table: ")
                    print()

                    if w=="":
                        print("Enter Something")
                        break

                    print("Heading Row in Selected Table: \n")
                    cursor.execute("show columns from {}".format(w))
                    for i in cursor:
                        print(i[0],end=" | ")
                    print()
                    print()

                    print("Student Data in Selected Table: \n")
                    cursor.execute("select * from {}".format(w))
                    for i in cursor:
                        print(i)
                    print()

                else:
                    print("No Table Found\n")
                    continue

                y=int(input("Enter 0 to show all Fees databases or 1 to go to Main Menu: "))
                if y==1:
                    Main()
                    break
    elif x==1:
        New_Database()
        
    elif x==2:
        Table()
        
    elif x==3:
        Database_Del()
        
    elif x==4:
        Table_Del()

    elif x==5:
        Data_Entry()

    elif x==6:
        Data_Del()

    elif x==7:
        print()
        print("                                                           THANKS")
    else:
        print()
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
    k=0
    while k==0:

        a=input("Enter Name of the New Fees Database \nDo not use names which are already present in Fees Database list:\n")
        cursor.execute("create database {}".format(a))
        print()
        print("Fees Database Created\n")
        Database_show()

        cursor.execute("commit")

        b=int(input("Enter 0 to do Table Creation in New Fees Database or 1 to goto Main Menu: "))
        if b==0:
            Table()
        else:
            break

        k=int(input("Enter 0 to create new Fees database or 1 to stop: "))
        print()

    Main()
    
def Table():
    print("                                                       TABLE CREATION MENU\n")
    Database_show()
    k=0
    while k==0:

        c=input("Enter name of the Fees Database in which u want to create table: ")
        cursor.execute("use {}".format(c))
        cursor.execute("show tables")
        lst=cursor.fetchall()
        print("Tables =\n")
        print(lst)
        print()

        d=input("Enter Name of new Table= ")
        print()
        e=input('''Enter Row Heading with specified data type(Ex:rollno int,name char(50),fees decimal(6,2)) to add in the Table :
Note: Do not use special character like full stop,etc and do not use space b/t Row Heading! \n''')
        print()
        cursor.execute("create table {}({})".format(d,e))
        print("Heading Row Created Successfully\n")

        cursor.execute("commit")

        cursor.execute("select * from {}".format(d))
        for i in cursor:
            print(i)

        f=int(input("Enter 0 to do Student Data Entry in New Fees Database or 1 to goto Main Menu: "))
        if f==0:
            Data_Entry()
        else:
            break

        k=int(input("Enter 0 to create new Fees database or 1 to stop: "))
        print()
    Main()

def Database_Del():
    print("                                                  FEES DATABASE DELETION MENU\n")
    k=0
    while k==0:

        Database_show()
        g=input("Enter Fees Database name which u want to Delete: ")
        print()
        cursor.execute("drop database {}".format(g))
        print("Fees Database Deleted Succesfully\n")
        Database_show()

        cursor.execute("commit")

        k=int(input("Enter 0 to delete more fees databases or 1 to stop: "))
        print()

    Main()

def Table_Del():
    print("                                                      TABLE DELETION MENU\n")
    k=0
    while k==0:

        Database_show()
        new=input("Enter Fees Database name in which u want to Delete the Table: ")
        print()
        cursor.execute("use {}".format(new))
        cursor.execute("show tables")
        lst=cursor.fetchall()
        print("Tables =\n")
        print(lst)
        print()

        new1=input("Enter Table name which u want to Delete: ")
        cursor.execute("drop table {}".format(new1))
        print("Table Deleted Succesfully\n")

        cursor.execute("show tables")
        lst=cursor.fetchall()
        print("Tables =\n")
        print(lst)
        print()

        cursor.execute("commit")

        k=int(input("Enter 0 to delete more Table or 1 to stop: "))
        print()

    Main()

def Data_Entry():
    print("                                                     STUDENT DATA ENTRY MENU\n")
    k=1
    while k==1:

        Database_show()
        h=input("Enter Fees Database: ")
        print()
        cursor.execute("use {}".format(h))
        cursor.execute("show tables")
        lst=cursor.fetchall()
        print("Tables =\n")
        print(lst)
        print()

        if len(lst)>0:

            k=input("Enter Table: ")

            print("Heading Row in Selected Database: \n")
            cursor.execute("use {}".format(h))
            cursor.execute("show columns from {}".format(k))
            for i in cursor:
                print(i[0],end=" | ")
            print()
            print()

            print("Student Data in Selected Fees Database: \n")
            cursor.execute("select * from {}".format(k))
            for i in cursor:
                print(i)
            print()

            l=0
            while l==0:
                m=input(f'''Enter Student Data as in sequence with Heading Rows
Note: Apply round brackets at starting and ending of entry
      Use inverted commas for string
      Seperate Data by commas
      u can enter multiple entry at same time by seperating them by commas
      EX: (1,"Abhi",300),(2,"Java",4554)\n''')
                cursor.execute("Insert into {} value{}".format(k,m))
                print("Student Data inserted Successfully\n")
                print()

                print("Student Data in Selected Database: ")
                cursor.execute("select * from {}".format(k))
                for i in cursor:
                    print(i)
                print()

                cursor.execute("commit")

                l=int(input("Enter 0 to do more Student Data Entry or 1 to take new fees database or 2 to stop: "))
                print()
            k=l
            print()
        else:
            print("No table found")
            Data_Entry()
    Main()

def Data_Del():
    print("                                                    STUDENT DATA DELETION MENU\n")
    k=0
    while k==0:

        Database_show() 
        n=input("Enter Fees Database Name in which u want to Delete: ")
        cursor.execute("use {}".format(n))
        cursor.execute("show tables")
        lst=cursor.fetchall()
        print("Tables =\n")
        print(lst)
        print()

        if len(lst)>0:

            o=input("Enter Name of the table: ")
            print()

            print("Rows in Selected Database: \n")
            cursor.execute("use {}".format(n))
            cursor.execute("show columns from {}".format(o))
            l=[]
            for i in cursor:
                print(i[0],end=" | ")
                l+=i
            print()
            print()

            print("Student Data in",o,"table :\n")
            cursor.execute("select * from {}".format(o))
            for i in cursor:
                print(i)
            print()

            p=input(f"Enter {l[0]} which u want to Delete\nIf Data does not exist press Enter! : \n")
            print()
            cursor.execute("delete from {} where {}={}".format(o,l[0],p))   
            cursor.execute("select * from {}".format(o))

            print("Now Data in",o,":\n")
            for i in cursor:
                print(i)
            print()

            cursor.execute("commit")

            k=int(input("Enter 0 to delete more Student Data Entry or 1 to stop: "))
            print()

        else:
            Data_Del()
    Main()
    
Main()
