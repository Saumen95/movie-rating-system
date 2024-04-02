from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Movie
from .models import Rating,Profile
from django.contrib.auth.models import User

# You can customize these forms if needed
class UserRegisterForm(UserCreationForm):
    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile.objects.get(user=user)
            profile.phone_number = self.cleaned_data['phone_number']
            profile.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number']

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

