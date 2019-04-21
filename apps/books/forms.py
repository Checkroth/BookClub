from django import forms

from .models import Book, BookProgress


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'link', 'page_count']


class BookProgressForm(forms.ModelForm):
    class Meta:
        model = BookProgress
        fields = ['user', 'book', 'pages_read']

    def clean(self):
        if self.cleaned_data.get('book'):
            pages_read = self.cleaned_data['pages_read']
            book = self.cleaned_data['book']
            if pages_read > book.page_count:
                raise forms.ValidationError(
                    {'pages_read': 'Cannot read more pages than the book has'})
