from django.db import models
from django.contrib.auth.models import User
from toys.models import Toy

# Create your models here.


class Order(models.Model):
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=False, default='')
    qty = models.IntegerField(blank=False, default=1)

# show the name in the database, make it into a string
    def __str__(self):
        return f"Purchase for Toy#{self.toy.id} by user#{self.user.id}"
