from django.contrib import admin
from .models import Movie, Rating  # Import your models here

# Register your models here.
admin.site.register(Movie)
admin.site.register(Rating)  # Do this for any other models you want in the admin


