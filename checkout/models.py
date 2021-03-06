from django.db import models
from django.contrib.auth.models import User
from toy.models import Toy


class Purchase(models.Model):
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=False)
    qty = models.IntegerField(blank=False)
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"Purchased toy#{self.toy_id} by user#{self.user_id} on {self.purchase_date}"

    def save(self, *args, **kwargs):
        self.total = self.price * self.qty
        super().save(*args, **kwargs)
