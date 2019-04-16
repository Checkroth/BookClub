from django import forms

from .models import Book, BookProgress


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'link', 'page_count']


class BookProgressForm(forms.ModelForm):
    class Meta:
        model = BookProgress
        fields = ['user', 'pages_read']
        widgets = {'user': forms.HiddenInput()}
