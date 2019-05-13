from collections import defaultdict
from typing import Iterator

from .template_types import (BookData, book_data_from_book,
                             ProgressData, progress_data_from_progress)


class BookApplication:
    def __init__(self,
                 book_repo,
                 book_progress_repo):
        self.book_repo = book_repo
        self.book_progress_repo = book_progress_repo

    def _get_all_books(self) -> Iterator[BookData]:
        books = self.book_repo.get_books()
        current_reader_counts = self.book_progress_repo.get_current_reader_counts_by_book()
        finished_reader_counts = self.book_progress_repo.get_finished_reader_counts_by_book()
        book_counts = defaultdict(dict)
        for reader in current_reader_counts:
            book_counts[reader['book_id']]['current_readers'] = reader['current_readers']
        for reader in finished_reader_counts:
            book_counts[reader['book_id']]['finished_readers'] = reader['finished_readers']
        for book in books:
            yield book_data_from_book(book,
                                      current_readers=book_counts[book.id]['current_readers'],
                                      finished_readers=book_counts[book.id]['finished_readers'])

    def get_all_books(self) -> Iterator[BookData]:
        # TODO:: order by -> distinct('pk') when a real db backend is determined
        return sorted(self._get_all_books(), key=lambda book: -book.current_readers)

    def get_book(self, pk):
        book = self.book_repo.get_book(pk)
        if book:
            return book_data_from_book(book, num_readers=book.number_of_readers)
        else:
            return None

    def get_top_books(self, number_of_books: int) -> Iterator[BookData]:
        books = self.book_repo.get_books()[:number_of_books]
        """
        TODO :: Return to generators when db backend supports `distinct on`
        for book in books[:number_of_books]:
            yield book_data_from_book(book, num_readers=book.number_of_readers)
        """
        books = [book_data_from_book(book, num_readers=book.number_of_readers)
                 for book in books]
        return sorted(books, key=lambda book: -book.num_readers)

    def get_all_progresses(self, book_id: int) -> Iterator[ProgressData]:
        all_progresses = self.book_progress_repo.get_all_progresses_by_percent(
            book_id)
        for progress in all_progresses:
            yield progress_data_from_progress(progress)
