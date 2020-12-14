from django.db import models
from toys.models import Toy
from django.contrib.auth.models import User

rating = (
    (1, '1 star'),
    (2, '2 stars'),
    (3, '3 stars'),
    (4, '4 stars'),
    (5, '5 stars')
)

# Create your models here.
class Review(models.Model):
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rating, default=3)
    desc = models.TextField(blank=False)

#show the name in the database, make it into a string
    def __str__(self):
        return self.title 
