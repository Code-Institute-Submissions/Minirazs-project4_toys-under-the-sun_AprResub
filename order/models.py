from django.db import models
from django.contrib.auth.models import User
from toy.models import Toy


class Order(models.Model):
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=False, default='')
    qty = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return f"Purchase for Toy#{self.toy.id} by user#{self.user.id}"
