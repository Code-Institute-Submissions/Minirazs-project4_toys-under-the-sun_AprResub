from django.db import models
from django.contrib.auth.models import User
from toy.models import Toy

# Create your models here.


class Purchase(models.Model):
    toy_id = models.ForeignKey(Toy, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=False)
    qty = models.IntegerField(blank=False)

    def __str__(self):
        return f"Purchased toy#{self.toy_id} by user#{self.user_id} on {self.purchase_date}"
