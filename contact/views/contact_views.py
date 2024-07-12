from django.shortcuts import render, redirect
from contact.forms import ClientForm,ClientLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def Home(request):
    return render(request,'contact/index.html')


def SignUpIn(request):
    if request.method == 'POST':
        loginForm = ClientLoginForm(request.POST)
        if loginForm.is_valid():
            name = loginForm.cleaned_data['name']
            password = loginForm.cleaned_data['password']
            user = authenticate(request, username=name, password=password)
            if user:
                login(request, user)    
                return redirect("/dashboard")

        cadastrarForm = ClientForm(request.POST)
        if cadastrarForm.is_valid():
            name = cadastrarForm.cleaned_data['name']
            email = cadastrarForm.cleaned_data['email']
            password = cadastrarForm.cleaned_data['password']
            user = User.objects.create_user(name, email, password)
            login(request, user)    
            return redirect("/dashboard")
    else:
        loginForm = ClientLoginForm()
        cadastrarForm = ClientForm()

    return render(request,'contact/login.html',{'login':loginForm, 'cadastrar':cadastrarForm})
