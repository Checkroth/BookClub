from typing import Iterator, Optional
from django.db.models import Count

from .models import Book, BookProgress


class BookRepository:
    def __init__(self,
                 model_book=Book):
        self.model_book = model_book

    def get_books(self,
                  name: str = None,
                  link: str = None,
                  page_count: int = None) -> Iterator[Book]:
        books = self.model_book.objects.all()
        if name:
            books.filter(name=name)
        if link:
            books.filter(link=link)
        if page_count is not None:
            books.filter(page_count=page_count)
        books = books.annotate(number_of_readers=Count('user_progresses'))
        return books

    def get_book(self,
                 pk=int) -> Optional[Book]:
        try:
            return self.model_book.objects.filter(
                pk=pk).annotate(number_of_readers=Count('user_progresses')).get()
        except self.model_book.DoesNotExist:
            return None


class BookProgressRepository:
    def __init__(self,
                 model_book_progress=BookProgress):
        self.model_book_progress = model_book_progress

    def get_all_progresses_by_percent(self, book_id):
        progresses = self.model_book_progress.objects.filter(book_id=book_id)
        progresses = progresses.order_by('-percent_progress')
        progresses.prefetch_related('user')
        return progresses

    def get_existing_progress(self, user_id, book_id) -> BookProgress:
        try:
            return self.model_book_progress.objects.get(user_id=user_id,
                                                        book_id=book_id)
        except self.model_book_progress.DoesNotExist:
            return None

    def get_current_reader_counts_by_book(self):
        return self.model_book_progress.objects.filter(percent_progress__lt=100).values(
            'book_id').annotate(current_readers=Count('book_id'))

    def get_finished_reader_counts_by_book(self):
        return self.model_book_progress.objects.filter(percent_progress=100).values(
            'book_id').annotate(finished_readers=Count('book_id'))

    def get_current_readers(self, book_id):
        qs = self.model_book_progress.objects.filter(book_id=book_id)
        return qs.filter(percent_progress__lte=100)

    def get_finished_readers(self, book_id):
        qs = self.model_book_progress.objects.filter(book_id=book_id)
        return qs.filter(pages_read=100)
