from django.contrib import admin
from .models import Movie, Rating  # Import your models here
from .models import Profile



# Register your models here.
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Rating)  # Do this for any other models you want in the admin


