from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
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
