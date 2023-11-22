import mysql.connector
from tkinter import *
from tkinter import messagebox


# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1702940929",
    database="library_management_Application",
)
cursor = db.cursor()

# Create library table if not exists
cursor.execute(
    "CREATE TABLE IF NOT EXISTS books (Id INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(255), Author VARCHAR(255), Available BOOLEAN)"
)
db.commit()

# Tkinter GUI
win = Tk()
win.title("Library Management System")
win.geometry("300x400")
win.config(bg="Light green")


# Functions
def add_book():
    title = title_entry.get()
    author = author_entry.get()

    if title and author:
        cursor.execute(
            "INSERT INTO books (Title, Author, Available) VALUES (%s, %s, %s)",
            (title, author, True),
        )
        db.commit()
        messagebox.showinfo("Success", "Book added successfully.")
    else:
        messagebox.showerror("Error", "Both Title and Author are required.")


def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    if books:
        for book in books:
            book_list = f" ID:  {book[0]}\n Title:  {book[1]}\n Author:  {book[2]}\n Available:  {book[3]}"

        messagebox.showinfo("Books", book_list)
    else:
        messagebox.showinfo("Books", "No books available.")


def delete_book():
    book_id = book_id_entry.get()
    if book_id:
        cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        db.commit()
        messagebox.showinfo("Success", "Book deleted successfully.")
    else:
        messagebox.showerror("Error", "Please enter Book ID.")


def issue_book():
    book_id = book_id_entry.get()
    if book_id:
        cursor.execute(
            "SELECT * FROM books WHERE id = %s AND available = TRUE", (book_id,)
        )
        book = cursor.fetchone()
        if book:
            cursor.execute(
                "UPDATE books SET available = FALSE WHERE id = %s", (book_id,)
            )
            db.commit()
            messagebox.showinfo("Success", "Book issued successfully.")
        else:
            messagebox.showerror("Error", "Book not available or invalid Book ID.")
    else:
        messagebox.showerror("Error", "Please enter Book ID.")


def return_book():
    book_id = book_id_entry.get()
    if book_id:
        cursor.execute(
            "SELECT * FROM books WHERE id = %s AND available = FALSE", (book_id,)
        )
        book = cursor.fetchone()
        if book:
            cursor.execute(
                "UPDATE books SET available = TRUE WHERE id = %s", (book_id,)
            )
            db.commit()
            messagebox.showinfo("Success", "Book returned successfully.")
        else:
            messagebox.showerror("Error", "Book not issued or invalid Book ID.")
    else:
        messagebox.showerror("Error", "Please enter Book ID.")


# GUI Elements
title_label = Label(win, text="Title:")
title_label.grid(row=0, column=0, padx=10, pady=10)
title_entry = Entry(win)
title_entry.grid(row=0, column=1, padx=10, pady=10)

author_label = Label(win, text="Author:")
author_label.grid(row=1, column=0, padx=10, pady=10)
author_entry = Entry(win)
author_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = Button(win, text="Add Book", command=add_book)
add_button.grid(row=2, column=1, columnspan=2, pady=10)
view_button = Button(win, text="View Books", command=view_books)
view_button.grid(row=3, column=1, columnspan=2, pady=10)

book_id_label = Label(win, text="Book ID:")
book_id_label.grid(row=4, column=0, padx=10, pady=10)
book_id_entry = Entry(win)
book_id_entry.grid(row=4, column=1, padx=10, pady=10)

delete_button = Button(win, text="Delete Book", command=delete_book)
delete_button.grid(row=5, column=1, columnspan=2, pady=10)

issue_button = Button(win, text="Issue Book", command=issue_book)
issue_button.grid(row=6, column=1, columnspan=2, pady=10)

return_button = Button(win, text="Return Book", command=return_book)
return_button.grid(row=7, column=1, columnspan=2, pady=10)


win.mainloop()
