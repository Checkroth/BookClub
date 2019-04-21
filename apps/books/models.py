from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField("Book Name", max_length=255)
    link = models.URLField("Link to book (amazon etc.)")
    page_count = models.IntegerField("Number of Pages")


class BookProgress(models.Model):
    # TODO:: validate that pages_read is <= page_count
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='book_progresses')
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='user_progresses')
    pages_read = models.PositiveIntegerField("Pages read",
                                             default=0)
