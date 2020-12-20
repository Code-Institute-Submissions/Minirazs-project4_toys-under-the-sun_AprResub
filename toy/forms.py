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

country = (
    ('UK', 'UK'),
    ('US', 'US'),
    ('Europe', 'Europe'),
    ('China', 'China'),
    ('Korea', 'Korea'),
    ('Japan', 'Japan'),
    ('SE Asia', 'SE Asia')
)

price = (
    (0-49, '$0-49'),
    (50-99, '$50-99'),
    (100-149, '$100-149'),
    (150-199, '$150-199'),
    (200, '> 200')
)


class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ('title', 'brand', 'price', 'country', 'age', 'desc',
                  'features')


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    age = forms.ChoiceField(choices=age, label="",
                            initial='', widget=forms.Select(), required=False)
    country = forms.ChoiceField(choices=country, label="",
                                initial='', widget=forms.Select(),
                                required=False)
    price = forms.ChoiceField(choices=price, label="",
                              initial='', widget=forms.Select(),
                              required=False)
