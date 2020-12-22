from django import forms
from .models import Toy
from cloudinary.forms import CloudinaryJsFileField

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


class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ('title', 'brand', 'price', 'country', 'age', 'desc',
                  'features', 'cover')

    cover = CloudinaryJsFileField()


class SearchForm(forms.Form):
    title = forms.CharField(label="Search by name",
                            max_length=100, required=False)

    country = forms.ChoiceField(choices=country, label="Country of Origin",
                                initial='', widget=forms.Select(),
                                required=False)

    age = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=age,
    )
