from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('<int:pk>/update_book_progress',
         login_required(views.update_book_progress),
         name='update_book_progress'),
    path('<int:pk>', login_required(views.view_book), name='view_book'),
    path('add', login_required(views.add_book), name='add_book'),
    path('', login_required(views.list_books), name='list_books')
]
