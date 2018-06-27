from locators.quotes_locator import QuoteLocators


class QuoteParser:
    """Given one of specific quote divs get info about given quote"""

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return "Quote {0}, by {1}".format(self.content, self.author)

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [e.string for e in self.parent.select(locator)]
