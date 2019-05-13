from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from apps import api

from .forms import BookForm, BookProgressForm
from .models import Book


def view_book(request, pk):
    book_app = api.get_book_app()
    book = get_object_or_404(Book, pk=pk)
    if not book:
        return HttpResponseNotFound()

    progress_repo = api.get_book_progress_repo()
    existing_progress = progress_repo.get_existing_progress(user_id=request.user.pk,
                                                            book_id=pk)
    if request.method == 'POST':
        progress_form = BookProgressForm(
            {'user': request.user.pk,
             'book': pk,
             'percent_progress': request.POST['percent_progress']},
            instance=existing_progress,
        )
        if progress_form.is_valid():
            progress_form.save()
    else:
        progress_form = BookProgressForm(
            {'percent_progress': existing_progress.percent_progress
             if existing_progress else 0})

    readers = book_app.get_all_progresses(pk)
    return render(request, 'book.html', {'book': book,
                                         'progress_form': progress_form,
                                         'readers': readers})


def list_books(request):
    book_app = api.get_book_app()
    books = book_app.get_all_books()
    return render(request,
                  'books.html',
                  {'books': books})


def add_book(request):
    """
    Register a new book
    Return errors if the input is invalid
    Return blank form on GET
    """
    if request.method == 'GET':
        form = BookForm()
        return render(request,
                      'add_book.html',
                      {'book_form': form})
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('books:view_book', pk=book.pk)

    return render(request,
                  'add_book.html',
                  {'book_form': form})
