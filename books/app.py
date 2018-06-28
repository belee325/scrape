import requests
from books.database.utils import database
from pages.book_page import BookPage

database.create_db()
page_content = requests.get('http://books.toscrape.com/catalogue/page-1.html').content
page = BookPage(page_content)
books = page.books
for i in range(2,51):
    page_content = requests.get('http://books.toscrape.com/catalogue/page-{}.html'.format(i)).content
    page = BookPage(page_content)
    books.extend(page.books)
#print('asdf\n')
#for content in page.books:
#    print(content)
#    database.add_books(content.title,content.rating,content.availability,content.price)
#print(database.list_books())


