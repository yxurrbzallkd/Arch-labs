from django import forms

class TheForm(forms.Form):
    msg = forms.CharField(label='Your message', max_length=100)