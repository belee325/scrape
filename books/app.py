import requests
from books.database.utils import database
from pages.book_page import BookPage
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger= logging.getLogger('scraping')

logger.info('Loading books list...')

database.create_db()
import_choice = input('load from database? y/n \n')
if import_choice == 'y':
    logger.info('loading from database')
    books = database.get_books()
else:
    logger.info('scraping website')
    page_content = requests.get('http://books.toscrape.com/catalogue/page-1.html').content
    page = BookPage(page_content)
    books = page.books
    page_count = int(page.page_count)

    for i in range(2, page_count + 1):
        page_content = requests.get('http://books.toscrape.com/catalogue/page-{}.html'.format(i)).content
        page = BookPage(page_content)
        books.extend(page.books)

    export_choice = input('save to db? y/n \n')
    if export_choice == 'y':
        logger.info('exporting to database')
        for book in books:
            database.add_books(book.title, book.rating, book.availability, book.price, book)
        logger.info('finished export to database')