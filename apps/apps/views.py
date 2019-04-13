from django.shortcuts import render
from . import api


def index(request):
    book_app = api.get_book_app()
    top_books = book_app.get_top_books(10)
    return render(request, 'index.html', {'top_books': top_books})
