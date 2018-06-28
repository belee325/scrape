from bs4 import BeautifulSoup
from books.parsers.book import BookParser
from books.locators.book_page_locator import BookPageLocator
import logging

logger = logging.getLogger('scraping.books_page')

class BookPage:
    def __init__(self, page):
        logger.debug('parsing page with beautiful soup html parser')
        self.page = BeautifulSoup(page,'html.parser')
    @property
    def books(self):
        logger.debug('Finding books in the page using {}'.format(BookPageLocator.BOOK_LOCATOR))
        locator = BookPageLocator.BOOK_LOCATOR
        book_items = self.page.select(locator)
        return [BookParser(b) for b in book_items]
    @property
    def page_count(self):
        logger.debug('Finding total number of pages available')
        locator = BookPageLocator.PAGE_COUNT_LOCATOR
        page_count_string = self.page.select_one(locator).string
        logger.debug('Found page count: {0}'.format(page_count_string))
        count = int(page_count_string.split()[3])
        logger.debug('Extracted page count {0}'.format(count))
        return count