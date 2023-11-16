import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1702940929",
    database= "library_management"
)

# # Create a cursor object to interact with the database
# cursor = db.cursor()

# # Create the database
# database = "library_management"

# cursor.execute(f"CREATE DATABASE {database}")
# print(f"Database '{database}' created successfully.")

query1='create table if not exists Books(Book_id int primary key,Title varchar(20),Author varchar(20),Publication_year varchar(20),Total_copies int,Available_copies int)'
query2='create table if not exists members(member_id int primary key,first_name varchar(20),last_name varchar(20),email varchar(20),phone varchar(20))'
query3='create table if not exists checkouts(checkout_id int primary key, book_id int, member_id int, checkout_date varchar(20), due_date varchar(20))'

cursor = db.cursor()
cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)
print('Table Created successfully' )



# Add a book to the library
def add_book(Book_id, Title, Author, Publication_year, Total_copies,Available_copies):
    sql = "INSERT INTO books (Book_id, Title, Author, Publication_year, Total_copies, Available_copies) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (Book_id, Title, Author, Publication_year, Total_copies ,Available_copies)
    cursor.execute(sql, values)
    db.commit()
   

# Add a member to the library
def add_member(member_id, first_name, last_name, email, phone):
    sql = "INSERT INTO members (member_id, first_name, last_name, email, phone) VALUES (%s, %s, %s, %s, %s)"
    values = (member_id, first_name, last_name, email, phone)
    cursor.execute(sql, values)
    db.commit()

# Check out a book
def checkout_book(checkout_id, book_id, member_id, checkout_date, due_date):
    sql = "INSERT INTO checkouts (checkout_id, book_id, member_id, checkout_date, due_date) VALUES (%s, %s, %s, %s, %s)"
    values = (checkout_id, book_id, member_id, checkout_date, due_date)
    cursor.execute(sql, values)
    db.commit()

# Display available books
def display_available_books():
    sql = "SELECT * FROM books WHERE available_copies > 0"
    cursor.execute(sql)
    result = cursor.fetchall()
    for book in result:
        print(f"Title: {book[1]}, Author: {book[2]}, Available Copies: {book[5]}")
display_available_books()


# Example Usage
add_book('101',"Strenth Of Material", "RK Bansal", 2003, "200", 2)
add_book('102',"Mechanics", "Khurmi", 2003, "200", 10)
add_book('103',"Mechanics", "Khurmi", 2003, "200", 10)
add_book('104',"Material Science", "KN Gupta", 1999, "200", 8)
add_book('105',"Fluid Mechanics", "SK Som", 1998, "200", 15)

# add_member
add_member("1", "Amit", "Singh", "amit@gmail.com", "8565871985")
add_member("2", "Sumit", "Singh", "sumit@gmail.com", "6365871985")
add_member("3", "Arun", "Yadav", "arun@gmail.com", "6565871985")
add_member("4", "Saurabh", "Chauhan", "saurabh@gmail.com", "9565871985")
add_member("5", "Sangam", "Mauraya", "sangam@gmail.com", "8565871985")


# check out books
checkout_book('1001', '101', '101', '2023/10/01', '2023/10/13')
checkout_book('1002', '102', '102', '2023/10/02', '2023/10/15')
checkout_book('1003', '103', '103', '2023/10/04', '2023/10/18')
checkout_book('1004', '104', '104', '2023/10/08', '2023/10/15')
checkout_book('1005', '105', '105', '2023/10/04', '2023/10/17')


# Close the database connection
db.close()
