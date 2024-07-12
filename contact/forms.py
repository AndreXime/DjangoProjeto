from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    admin = forms.BooleanField(required=False)