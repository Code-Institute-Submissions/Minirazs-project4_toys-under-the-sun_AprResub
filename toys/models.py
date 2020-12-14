from django.db import models

# Create your models here.
class Toy(models.Model):
    title = models.CharField(blank=False, max_length=255)
    price = models.FloatField(blank=False)
    desc = models.TextField(blank=False)

#show the name in the database, make it into a string
    def __str__(self):
        return self.title 
