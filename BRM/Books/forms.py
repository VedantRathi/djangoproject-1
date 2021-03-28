from django import forms

class newForm(forms.Form):
    name=forms.CharField(max_length=60,label='Name')
    author=forms.CharField(max_length=60,label='Author')
    price=forms.FloatField(label='Price')
    publisher=forms.CharField(max_length=60,label='Publisher')

class searchForm(forms.Form):
    name=forms.CharField(max_length=60,label='Name')
