from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'rating', 'review')
        widgets = {
            'review': forms.Textarea(attrs={
                'rows': '4',
                'cols': '90',
                'maxlength': '200',
            }),
        }
