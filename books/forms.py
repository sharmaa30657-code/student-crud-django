from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'year', 'rating', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title...'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author name...'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Publication year...', 'min': 1000, 'max': 2100}),
            'rating': forms.NumberInput(attrs={'placeholder': '0.0 - 10.0', 'min': 0, 'max': 10, 'step': 0.1}),
            'description': forms.Textarea(attrs={'placeholder': 'Write a short description...', 'rows': 4}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and (rating < 0 or rating > 10):
            raise forms.ValidationError("Rating must be between 0 and 10.")
        return rating
