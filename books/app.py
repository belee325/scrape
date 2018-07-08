import requests
from books.database.utils import database
from pages.book_page import BookPage
import logging
import aiohttp
import asyncio
import async_timeout
import time

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')
logger = logging.getLogger('scraping')


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            # print(response.status)
            print('fetch took {}'.format(time.time() - page_start))
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_task = asyncio.gather(*tasks)
        return await grouped_task


database.create_db()
import_choice = input('load from database? y/n \n')

if import_choice == 'y':
    logger.info('loading from database')
    books = database.get_books()
else:
    logger.info('getting first page and page count')
    page_content = requests.get('http://books.toscrape.com/catalogue/page-1.html').content
    page = BookPage(page_content)
    books = page.books
    page_count = int(page.page_count)
    loop = asyncio.get_event_loop()
    urls = ['http://books.toscrape.com/catalogue/page-{0}.html'.format(i) for i in range(2, page_count)]
    pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
    for page_content in pages:
        page = BookPage(page_content)
        books.extend(page.books)
    export_choice = input('save to db? y/n \n')
    if export_choice == 'y':
        logger.info('exporting to database')
        for book in books:
            database.add_books(book.title, book.rating, book.availability, book.price, book)
        logger.info('finished export to database.')
