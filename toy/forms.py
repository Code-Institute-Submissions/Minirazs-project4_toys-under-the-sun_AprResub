from django import forms
from .models import Toy

age = (
    ('0-2 years', '0-2 years'),
    ('3-4 years', '3-4 years'),
    ('5-7 years', '5-7 years'),
    ('8-11 years', '8-11 years'),
    ('12-14 years', '12-14 years'),
    ('14 years+', '14 years+')
)


class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ('title', 'brand', 'price', 'country', 'age', 'desc',
                  'features')


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    age = forms.ModelChoiceField(queryset=age, required=False)
