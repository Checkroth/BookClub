from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import render, redirect

from apps import api

from .forms import BookForm, BookProgressForm


def update_book_progress(request, pk):
    if request.method != 'POST':
        return HttpResponseNotAllowed()

    form = BookProgressForm({'user': request.user.pk,
                             'book': pk,
                             **request.POST})
    import pdb; pdb.set_trace();
    if not form.is_valid():
        # add form error messages here
        print(form.errors)
    else:
        # add success message here
        print('success')
        form.save()
    return redirect('books:view_book', pk=pk)


def view_book(request, pk):
    book_repo = api.get_book_repo()
    book_app = api.get_book_app()
    book = book_repo.get_book(pk)
    if not book:
        return HttpResponseNotFound()

    readers = book_app.get_all_progresses(pk)
    progress_form = BookProgressForm({'user': request.user.pk,
                                      'book': pk})
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
            form.save()
            return redirect('books:view_book', pk=form.pk)

    return render(request,
                  'add_book.html',
                  {'book_form': form})
