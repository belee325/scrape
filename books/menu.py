from app import books
import logging
logger = logging.getLogger('scraper.menu')
USER_CHOICE='''
Enter one of the following
-'b' to look at 5 star books
-'c' to look at cheapest books
-'n' to look at next available book
-'q' to quit
'''

def best_book():
    logger.info('Finding best book based on rating')
    sorted_books = sorted(books, key= lambda x : x.rating*-1)[:10]
    for book in sorted_books:
        print(book)

def cheapest_book():
    logger.info('Finding cheapest books')
    cheapest_books = sorted(books, key=lambda x: x.price)
    for book in cheapest_books:
        print(book)

books_generator = (x for x in books)

def next_book():
    print(next(books_generator))

USER_CHOICES = {
    'b': best_book,
    'c': cheapest_book,
    'n': next_book
}


def menu():
    choice = input(USER_CHOICE)
    while(choice!='q'):
        if choice in ('b','c','n'):
            USER_CHOICES[choice]()
        else:
            print('enter a valid choice')
        choice = input(USER_CHOICE)
    logger.info('Terminating program with choice: `{0}`'.format(choice))

menu()