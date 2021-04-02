from django import forms
from .models import Toy
from cloudinary.forms import CloudinaryJsFileField

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


class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ('title', 'brand', 'price', 'country', 'age', 'category',
                  'desc', 'features', 'cover')

    cover = CloudinaryJsFileField()


class SearchForm(forms.Form):
    title = forms.CharField(label="Search by name",
                            max_length=100, required=False)

    category = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=category,
    )

    age = forms.MultipleChoiceField(
        label="Age Group",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=age,
    )

    country = forms.MultipleChoiceField(
        label="Country of Origin",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=country,
    )
