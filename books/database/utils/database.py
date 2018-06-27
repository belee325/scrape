from books.database.utils.database_connection import DatabaseConnection
import sqlite3

def create_db():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books(title text primary key, rating text, availability text, price real)')


def add_books(title, rating, availability, price):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO books VALUES (?,?,?,?)', (title, rating, availability, price))
        except sqlite3.IntegrityError as e:
            print("book already exists")

def list_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT* FROM books')
        books=[{"Title":row[0], 'Rating':row[1], 'Stock':row[2], "Price":row[3]} for row in cursor.fetchall()]
        return books



def delete_books(title):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE title = ?', (title, _))
