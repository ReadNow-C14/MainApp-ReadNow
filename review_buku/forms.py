from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget = forms.Textarea(), required=True)
    class Meta:
        model = Review
        fields = ['rating', 'comment']