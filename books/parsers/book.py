#for a given book, get info
from books.locators.book_attributes_locator import BookAttributesLocator
import re
class BookParser:
    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return """Title: {0}\nRating: {1}\nStock: {2}\nPrice:{3}\n""".format(self.title, self.rating, self.availability, self.price)
    @property
    def title(self):
        locator = BookAttributesLocator.TITLE_LOCATOR
        return self.parent.select_one(locator).attrs['title']

    @property
    def price(self):
        locator = BookAttributesLocator.PRICE_LOCATOR
        #get rid of pound sign?
        patt = '[0-9]+\.[0-9]+'
        match = re.search(patt,self.parent.select_one(locator).string)
        return float(match[0])

    @property
    def rating(self):
        locator = BookAttributesLocator.RATING_LOCATOR
        #need to parse out correct string
        rating_element = self.parent.select_one(locator).attrs['class']
        return rating_element[1]

    @property
    def image(self):
        pass

    @property
    def availability(self):
        locator = BookAttributesLocator.AVAILABILITY_LOCATOR
        availability_element = self.parent.select_one(locator)
        availability_text = availability_element.text
        return availability_text.strip()
