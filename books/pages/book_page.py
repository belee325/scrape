from bs4 import BeautifulSoup
from books.parsers.book import BookParser
from books.locators.book_page_locator import BookPageLocator

class BookPage:
    def __init__(self, page):
        self.page = BeautifulSoup(page,'html.parser')
    @property
    def books(self):
        locator = BookPageLocator.BOOK_LOCATOR
        book_items = self.page.select(locator)
        return [BookParser(b) for b in book_items]