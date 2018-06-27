from app import books

USER_CHOICE='''
Enter one of the following
-'b' to look at 5 star books
-'c' to look at cheapest books
-'n' to look at next available book
-'q' to quit
'''


def best_book():
    sorted_books = sorted(books, key= lambda x : x.rating*-1)[:10]
    for book in sorted_books:
        print(book)
def cheapest_book():
    pass


choice = input(USER_CHOICE)

while(choice!='q'):
    if choice == 'b':
        best_book()
    choice = input(USER_CHOICE)