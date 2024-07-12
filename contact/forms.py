from django import forms
from contact.models import Client

class ClientForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    admin = forms.BooleanField(required=False,label='Você é admin?', widget=forms.CheckboxInput(attrs={'class': 'checkmark'}))

    class Meta:
        model = Client
        fields = ("name","email","password","admin")

class ClientLoginForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    class Meta:
        model = Client
        fields = {"name","password"}