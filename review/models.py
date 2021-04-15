from django.db import models
from toy.models import Toy
from django.contrib.auth.models import User

rating = (
    (1, '1 star'),
    (2, '2 stars'),
    (3, '3 stars'),
    (4, '4 stars'),
    (5, '5 stars')
)


class Review(models.Model):
    title = models.CharField(blank=False, max_length=255, default=' ')
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rating, default=3)
    review = models.TextField(blank=False, default=' ')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
