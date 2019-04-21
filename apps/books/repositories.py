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

    def get_books_by_number_of_readers(self):
        books = self.get_books()
        return books.order_by('-user_progresses')


class BookProgressRepository:
    def __init__(self,
                 model_book_progress=BookProgress):
        self.model_book_progress = model_book_progress

    def get_all_progresses_by_pages_read(self, book_id):
        progresses = self.model_book_progress.objects.filter(book_id=book_id)
        progresses = progresses.order_by('-pages_read')
        progresses.prefetch_related('user')
        return progresses
