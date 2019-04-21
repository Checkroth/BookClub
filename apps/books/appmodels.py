from typing import Iterator

from .template_types import (BookData, book_data_from_book,
                             ProgressData, progress_data_from_progress)


class BookApplication:
    def __init__(self,
                 book_repo,
                 book_progress_repo):
        self.book_repo = book_repo
        self.book_progress_repo = book_progress_repo

    def get_all_books(self) -> Iterator[BookData]:
        books = self.book_repo.get_books()
        for book in books:
            yield book_data_from_book(book, num_readers=book.number_of_readers)

    def get_book(self, pk):
        book = self.book_repo.get_book(pk)
        if book:
            return book_data_from_book(book, num_readers=book.number_of_readers)
        else:
            return None

    def get_top_books(self, number_of_books: int) -> Iterator[BookData]:
        books = self.book_repo.get_books_by_number_of_readers()
        for book in books[:number_of_books]:
            yield book_data_from_book(book, num_readers=book.number_of_readers)

    def get_all_progresses(self, book_id: int) -> Iterator[ProgressData]:
        all_progresses = self.book_progress_repo.get_all_book_progresses_by_pages_read(
            book_id)
        for progress in all_progresses:
            yield progress_data_from_progress(progress)
