#for a given book, get info
from books.locators.book_attributes_locator import BookAttributesLocator
import re
import logging

RATING_MAP={
    'One':1,
    'Two':2,
    'Three':3,
    'Four':4,
    'Five':5
}

logger = logging.getLogger('scraping.book_parser')

class BookParser:
    def __init__(self,parent):
        logger.debug('New book parser created from parent')
        self.parent = parent

    def __repr__(self):
        return """Title: {0}\nRating: {1}\nStock: {2}\nPrice: {3}\n""".format(self.title, self.rating, self.availability, self.price)
    @property
    def title(self):
        logger.debug('Finding book title')
        locator = BookAttributesLocator.TITLE_LOCATOR
        title = self.parent.select_one(locator).attrs['title']
        logger.debug('Found book title `{}`'.format(title))
        return title

    @property
    def price(self):
        logger.debug('Finding price')
        locator = BookAttributesLocator.PRICE_LOCATOR
        #get rid of pound sign?
        patt = '[0-9]+\.[0-9]+'
        match = re.search(patt,self.parent.select_one(locator).string)
        price = match.group(0)
        logger.debug('Found price: `{}`'.format(price))
        return price

    @property
    def rating(self):
        logger.debug('Finding rating')
        locator = BookAttributesLocator.RATING_LOCATOR
        #need to parse out correct string
        rating_element = self.parent.select_one(locator).attrs['class']
        rating = RATING_MAP[rating_element[1]]
        logger.debug('Found rating: `{}`'.format(rating))
        return rating
    @property
    def image(self):
        pass

    @property
    def availability(self):
        logger.debug('Finding availability')
        locator = BookAttributesLocator.AVAILABILITY_LOCATOR
        availability_element = self.parent.select_one(locator)
        availability_text = availability_element.text.strip()
        logger.debug('Found availability: `{}`'.format(availability_text))
        return availability_text
