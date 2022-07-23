'''
    Title: whatabook.py
    Author: Robert D Boggs
    Date: 07/20/22
    Description: a program that lets you access the WhatABook Database and make changes to your account
    Attribution: Forta, B. (2020). SQL in 10 Minutes a Day, Sams Teach Yourself. Sams Publishing.
                 Sadalage, P., & Fowler, M. (2012). NoSQL Distilled.
'''

#import statements
import sys
import mysql.connector
from mysql.connector import errorcode

#Connects to the database
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#Displays the main menu

def show_menu():
    print("\n Whatabook Main Menu ")
    print("\n 1. View Books\n  2. View Store Locations\n  3. View My Account\n 4. Exit Program")

    try:
        menu_id = int(input(" Enter your selection as a number "))
        return menu_id

    except ValueError: 
        print(" INVALID ENTRY")

        sys.exit(0)
 
#Displays available books
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, details, author FROM book")
    books = _cursor.fetchall()
    print("\n The following is a list of our currently available books ")
    for book in books:
        print("\n\n Book ID: {} Book Name: {} Book Details: {} Book Author: {}".format(book[0], book[1], book[2], book[3]))

#Display store location
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale FROM store")
    stores = _cursor.fetchall()
    print("\n Displaying our current store locations ")

    for store in stores:
        print("\n\n Store ID: {}\n Store Locale: {}\n ".format(store[0], store[1])) 

#Creates secure login object
def validate_user():
    try:
        user_id = int(input(" Select User ID 1, 2, or 3"))

        if user_id < 0 or user_id > 3:
            print("ERROR: User ID has not been created yet!")
        return user_id
   
    except ValueError:
        print("ERROR: User ID has not been created yet!")
    sys.exit(0)

#Main account menu
def show_account_menu():

    try:
        print(" Account Menu ")
        print(" 1. Wishlist\n     2. Add Book\n    3. Main Menu ")
        choice = int(input(" Make A Selection "))

        return choice
    
    except ValueError: 
        print("ERROR: Please enter 1, 2, or 3 ")
        sys.exit(0)

#Display the wishlist
def show_wishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author "
    + "FROM wishlist " + "INNER JOIN user ON wishlist.user_id = user.user_id "
    + "INNER JOIN book ON wishlist.book_id = book.book_id" + "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()
    print("\n Displaying items in user's wishlist")

    for book in wishlist:
        print("\n\n Book Name: {}\n Author: {}\n ".format(book[4], book[5]))

#Displays available books
def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, details, author  " + "FROM book " + "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    print(query)
    _cursor.execute(query)
    books_to_add = _cursor.fetchall()
    print("\n Displaying books not currently in wishlist ")

    for book in books_to_add:
        print("\n Book ID: {}\n Book Name: {} Author: {}".format(book[0], book[1], book[2]))

#Adds book to wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor() 
    print("Hello and Welcome to The Whatabook Bookstore")
    user_selection = show_menu()

    while user_selection != 4:
        #Jump to books
        if user_selection == 1:
            show_books(cursor)
            sys.exit(0)
        #Jump to Location
        if user_selection == 2:
            show_locations(cursor)
            sys.exit(0)
        #Validate user and jump to menu
        if user_selection == 3:
            users_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, users_id)

                if account_option == 2: 
                    show_books_to_add(cursor, users_id)
                    book_id = int(input(" Enter the book ID to be add to your wishlist "))
                    add_book_to_wishlist(cursor, users_id, book_id)
                    db.commit()
                    print("\n {} successfully added to your wishlist ".format(book_id))

                if account_option < 0 or account_option > 3:
                    print("Choose another option")

                account_option = show_account_menu()

            if user_selection < 0 or user_selection > 4:
                print("Choose another option")

            user_selection = show_menu()

        print("sa·yo·na·ra")


except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  INVALID ENTRY")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  INVALID ENTRY")

    else:
        print(err)

finally:

    db.close()
