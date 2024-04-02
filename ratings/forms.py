from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Movie
from .models import Rating

# You can customize these forms if needed
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars', 'comment','rating']
        widgets = {
            'stars': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(label='Search for movies', max_length=100)

