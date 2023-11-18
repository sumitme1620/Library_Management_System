import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1702940929",
    database="library_management_system",
)
query = "create table if not exists data(ID int,Book_name varchar(20),Author_name varchar(20),Book_code int ,Total int ,Subject varchar(20))"
cur = con.cursor()
cur.execute(query)
print("Created")


def addbooks():
    ID = input("Enter Your ID : ")
    book_name = input("Enter Book Name : ")
    author_name = input("Enter Author Name : ")
    book_code = input("Enter Book Code : ")
    total = input("Enter Total Books : ")
    subject = input("Enter Subject of Books : ")

    res = con.cursor()
    sql = "insert into data (id,book_name,author_name,book_code,total,subject) values (%s,%s,%s,%s,%s,%s)"
    values = (ID, book_name, author_name, book_code, total, subject)
    res.execute(sql, values)
    con.commit()
    print("\n")
    print("Books Added Successfully")


def selectbooks():
    res = con.cursor()
    sql = "SELECT * from data"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    print(
        tabulate(
            result,
            headers=["ID", "BOOK NAME", "AUTHOR NAME", "BOOK CODE", "TOTAL", "SUBJECT"],
        )
    )


def updatebooks():
    print("1.Book Name")
    print("2.Author Name")
    print("3.Book Code")
    print("4.Total")
    print("5.Subject")
    option = int(input("\nWhich field you want to update?:"))
    if option == 1:
        pid = input("Enter Your ID:")
        book_name = input("Enter Your Book Name:")
        cur = con.cursor()
        sql = "UPDATE data set book_name=%s where id=%s"
        cur.execute(sql, (book_name, pid))

        con.commit()
        selectbooks()
        print("\n")
        print("Update Successfully")
    elif option == 2:
        pid = input("Enter Your ID:")
        author_name = input("Enter Your Author Name:")
        cur = con.cursor()
        sql = "UPDATE data set author_name=%s where id=%s"
        cur.execute(sql, (author_name, pid))
        con.commit()
        selectbooks()
        print("\n")
        print("Update Successfully")
    elif option == 3:
        pid = input("Enter Your ID:")
        book_code = input("Enter Your Book Code:")
        cur = con.cursor()
        sql = "UPDATE data set book_code=%s where pid=%s"
        cur.execute(sql, (book_code, pid))
        con.commit()
        selectbooks()
        print("\n")
        print("Update Successfully")
    elif option == 4:
        pid = input("Enter Your ID:")
        total = input("Enter Total Books:")
        cur = con.cursor()
        sql = "UPDATE data total=%s where id=%s"
        cur.execute(sql, (total, pid))
        con.commit()
        selectbooks()
        print("\n")
        print("Update Successfully")
    elif option == 5:
        pid = input("Enter Your ID:")
        subject = input("Enter Your Subject:")
        cur = con.cursor()
        sql = "UPDATE data set subject=%s where id=%s"
        cur.execute(sql, (subject, pid))
        con.commit()
        selectbooks()
        print("\n")
        print("Update Successfully")
    else:
        print("Invalid")


def deletebooks():
    pid = input("Enter Your ID:")
    res = con.cursor()
    sql = "delete from data where id=%s"
    res.execute(sql, (pid,))
    con.commit()
    print("\n")
    print("Books Deleted Successfully...!!!")


while True:
    print("\n")
    print("1.Add Books")
    print("2.Select Books")
    print("3.Update Books")
    print("4.Delete Books")
    print("5.Exit")
    print("\n")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        addbooks()
    elif choice == 2:
        selectbooks()
    elif choice == 3:
        updatebooks()
    elif choice == 4:
        deletebooks()
    elif choice == 5:
        quit()
    else:
        print("Invalid Option...!!!")
