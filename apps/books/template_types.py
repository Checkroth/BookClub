"""
Dataclass implementations for Django Models
Intended as a replacement for returning actual model instsances to templates,
    ideally to reduce unwanted queries in unexpected code blocks
"""

from dataclasses import dataclass


def book_data_from_book(book,
                        current_readers: int,
                        finished_readers: int):
    return BookData(pk=book.pk,
                    name=book.name,
                    link=book.link,
                    page_count=book.page_count,
                    current_readers=current_readers,
                    finished_readers=finished_readers)


@dataclass
class BookData:
    pk: int
    name: str
    link: str
    page_count: int
    current_readers: int
    finished_readers: int


def progress_data_from_progress(progress):
    return ProgressData(username=progress.user.username,
                        percent_progress=progress.percent_progress)


@dataclass
class ProgressData:
    username: str
    percent_progress: int
