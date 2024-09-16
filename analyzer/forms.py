from django import forms

class TextAnalysisForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50, 'maxlength': 250}))
from django import forms

class TextAnalysisForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50, 'maxlength': 250}))
