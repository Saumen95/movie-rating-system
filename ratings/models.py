from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    # Add more fields as necessary
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movies",null=True)

    def average_rating(self):
        ratings = self.rating_set.all()
        if ratings.count() == 0:
            return 0
        return sum(rating.stars for rating in ratings) / ratings.count()


class Rating(models.Model):
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    comment = models.TextField(blank=True)
    # Add more fields as necessary
    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
