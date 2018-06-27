import requests
from books.database.utils import database
from pages.book_page import BookPage

database.create_db()

page_content = requests.get('http://books.toscrape.com').content

page = BookPage(page_content)
for content in page.books:
    print(content)
    database.add_books(content.title,content.rating,content.availability,content.price)
print(database.list_books())


