from bs4 import BeautifulSoup
from locators.quotes_page_locator import QuotesPageLocators
from parsers.quote import  QuoteParser

class QuotesPage:
    def __init__(self,page):
        self.page = BeautifulSoup(page,'html.parser')
    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.page.select(locator)
        return [QuoteParser(e) for e in quote_tags]