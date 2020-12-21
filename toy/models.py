from django.db import models
from cloudinary.models import CloudinaryField

country = (
    ('UK', 'UK'),
    ('US', 'US'),
    ('Europe', 'Europe'),
    ('China', 'China'),
    ('Korea', 'Korea'),
    ('Japan', 'Japan'),
    ('SE Asia', 'SE Asia')
)

age = (
    ('0-2 years', '0-2 years'),
    ('3-4 years', '3-4 years'),
    ('5-7 years', '5-7 years'),
    ('8-11 years', '8-11 years'),
    ('12-14 years', '12-14 years'),
    ('14 years+', '14 years+')
)

# Create your models here.


class Toy(models.Model):
    title = models.CharField(blank=False, max_length=100, default='')
    brand = models.CharField(blank=False, max_length=50, default='')
    price = models.FloatField(blank=False, default='')
    country = models.CharField(choices=country, max_length=50, default='China')
    age = models.CharField(choices=age, max_length=50, default='5-7 years')
    desc = models.TextField(blank=False, default='')
    features = models.TextField(blank=False, default='')

# show the name in the database, make it into a string
    def __str__(self):
        return self.title
