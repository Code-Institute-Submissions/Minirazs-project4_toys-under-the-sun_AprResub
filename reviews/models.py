from django.db import models

rating = (
    (1, '1 star'),
    (2, '2 stars'),
    (3, '3 stars'),
    (4, '4 stars'),
    (5, '5 stars')
)

# Create your models here.
class Review(models.Model):
    title = models.CharField(blank=False, max_length=255)
    rating = models.IntegerField(choices=rating, default=3)
    desc = models.TextField(blank=False)

#show the name in the database, make it into a string
    def __str__(self):
        return self.title 
