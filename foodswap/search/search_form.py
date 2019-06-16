from django import forms

class SearchForm(forms.Form):
    post = forms.CharField(label='Search for food', max_length=100)