from django import forms
from .models import Toy


class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ('title', 'brand', 'price', 'country', 'age', 'desc',
                  'features')
