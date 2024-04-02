from django.shortcuts import render, redirect,get_object_or_404
from .forms import UserCreationForm, AuthenticationForm,RatingForm
from django.contrib.auth import login, authenticate
from .models import Movie,Rating
from django.contrib.auth.decorators import login_required
from .forms import MovieForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to your main page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'ratings/movie_list.html', {'movies': movies})

@login_required
def rate_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.movie = movie
            rating.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = RatingForm()
    return render(request, 'ratings/rate_movie.html', {'form': form, 'movie': movie})

@login_required
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                user=request.user,
                movie=movie,
                defaults={'rating': form.cleaned_data['rating']}
            )
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = RatingForm()

    return render(request, 'movies/movie_detail.html', {'movie': movie, 'form': form})

def movie_search(request):
    query = request.GET.get('q')
    movies = Movie.objects.filter(title__icontains=query)
    return render(request, 'ratings/movie_search.html', {'movies': movies})


@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            # You can add any additional fields or modifications here
            movie.save()
            return redirect('movie_list')  # Redirect to the movie list page
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})


@login_required
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id, user=request.user)  # Restricts access to the creator
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit_movie.html', {'form': form, 'movie': movie})

@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id, user=request.user)  # Restricts access to the creator
    if request.method == "POST":
        movie.delete()
        return redirect('movie_list')
    return render(request, 'confirm_delete.html', {'movie': movie})

