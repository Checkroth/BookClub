"""
Dataclass implementations for Django Models
Intended as a replacement for returning actual model instsances to templates,
    ideally to reduce unwanted queries in unexpected code blocks
"""

from dataclasses import dataclass


def book_data_from_book(book, num_readers: int):
    return BookData(pk=book.pk,
                    name=book.name,
                    link=book.link,
                    page_count=book.page_count,
                    num_readers=num_readers)


@dataclass
class BookData:
    pk: int
    name: str
    link: str
    page_count: int
    num_readers: int
