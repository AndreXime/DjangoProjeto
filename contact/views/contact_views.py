from django.shortcuts import render

def index(request):
    return render(request,'contact/index.html')

def login(request):
    return render(request,'contact/login.html')
