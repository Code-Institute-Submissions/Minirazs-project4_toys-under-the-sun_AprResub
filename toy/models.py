from django.db import models
from cloudinary.models import CloudinaryField

country = (
    ('UK & Europe', 'UK & Europe'),
    ('US & Canada', 'US & Canada'),
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

category = (
    ('Baby and Toddler toys', 'Baby and Toddler toys'),
    ('Action figure and Dolls', 'Action figures and Dolls'),
    ('Stuff toys', 'Stuff toys'),
    ('Craft and activities', 'Craft and activities'),
    ('Learning toys', 'Learning toys'),
    ('Electronics', 'Electronics')
)


class Toy(models.Model):
    title = models.CharField(blank=False, max_length=100, default='')
    brand = models.CharField(blank=False, max_length=50, default='')
    price = models.DecimalField(max_digits=10, decimal_places=3,
                                default=0, blank=False)
    country = models.CharField(choices=country, max_length=50, default='')
    age = models.CharField(choices=age, max_length=50, default='')
    category = models.CharField(choices=category, max_length=50,
                                default='')
    desc = models.TextField(blank=False, default='')
    features = models.TextField(blank=False, default='')
    cover = CloudinaryField()

    def __str__(self):
        return self.title
