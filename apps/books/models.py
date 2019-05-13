from django.db import models
from django.contrib.auth.models import User
from django.core import validators


class Book(models.Model):
    name = models.CharField("Book Name", max_length=255, unique=True)
    link = models.URLField("Link to book (amazon etc.)")
    page_count = models.IntegerField("Number of Pages")


class BookProgress(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='book_progresses')
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='user_progresses')
    percent_progress = models.PositiveIntegerField(
        "Progress",
        default=0,
        validators=[validators.MaxValueValidator(100)])

    class Meta:
        unique_together = (('user', 'book'))
