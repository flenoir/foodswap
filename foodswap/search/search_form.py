from django import forms

class SearchForm(forms.Form):
    post = forms.CharField(label='Your search', max_length=100)