/*
    Title: whatabook.init.sql
    Author: Robert D Boggs
    Date: 7/09/22
    Description: database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1005 W Burnside St. Portland, OR 97209');

/*
    insert book records 
*/

INSERT INTO book(book_name, author, details)
    VALUES('American Gods', 'Neil Gaiman', 'Fantasy');

INSERT INTO book(book_name, author, details)
    VALUES('The Way of Kings', 'Brandon Sanderson', 'Fantasy');

INSERT INTO book(book_name, author, details)
  VALUES('The Shadow of What Was Lost', 'James Islington', 'Fantasy');

INSERT INTO book(book_name, author, details)
  VALUES ('Leviathan Wakes', 'James S. A. Corey', 'Science-Fiction');

  

INSERT INTO book(book_name, author)
    VALUES('1984', 'George Orwell');

INSERT INTO book(book_name, author)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book(book_name, author)
    VALUES('To Kill A Mockingbird', 'Harper Lee');

INSERT INTO book(book_name, author)
    VALUES('Through the looking glass and What Alice Found There', 'Lewis Carroll');

INSERT INTO book(book_name, author)
    VALUES('War and Peace', 'Leo Tolstoy');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Talkamar', 'Deshrel');

INSERT INTO user(first_name, last_name)
    VALUES('Harry', 'Dresdin');

INSERT INTO user(first_name, last_name)
    VALUES('Waxilliam', 'Ladrian');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (1,3);

INSERT INTO wishlist(user_id, book_id)
    VALUES (2,6);

INSERT INTO wishlist(user_id, book_id)
    VALUES (3,8);