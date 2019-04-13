from books.appmodels import BookApplication
from books.repositories import BookRepository, BookProgressRepository


def get_book_app():
    return BookApplication(BookRepository(),
                           BookProgressRepository())


def get_book_repo():
    return BookRepository()
