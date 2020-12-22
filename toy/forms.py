from django import forms
from .models import Toy
from cloudinary.forms import CloudinaryJsFileField

age = (
    ('any', 'any'),
    ('0-2 years', '0-2 years'),
    ('3-4 years', '3-4 years'),
    ('5-7 years', '5-7 years'),
    ('8-11 years', '8-11 years'),
    ('12-14 years', '12-14 years'),
    ('14 years+', '14 years+')
)

country = (
    ('any', 'any'),
    ('UK', 'UK'),
    ('US', 'US'),
    ('Europe', 'Europe'),
    ('China', 'China'),
    ('Korea', 'Korea'),
    ('Japan', 'Japan'),
    ('SE Asia', 'SE Asia')
)

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ('title', 'brand', 'price', 'country', 'age', 'desc',
                  'features', 'cover')
    
    cover = CloudinaryJsFileField()


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    age = forms.ChoiceField(choices=age, label="",
                            initial='', widget=forms.Select(), required=False)
    country = forms.ChoiceField(choices=country, label="",
                                initial='', widget=forms.Select(),
                                required=False)

