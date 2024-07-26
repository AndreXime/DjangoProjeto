from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from contact.forms import ClientForm,ClientLoginForm
from contact.models import Client

def Home(request):
    return render(request,'contact/index.html')

def SignUpIn(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        loginForm = ClientLoginForm(request.POST)
        if loginForm.is_valid():
            name = loginForm.cleaned_data['name']
            password = loginForm.cleaned_data['password']
            user = authenticate(request, username=name, password=password)
            if user:
                login(request, user)
                if request.user.groups.filter(name='Administradores').exists():
                    return redirect("admin")
                else:
                    return redirect("dashboard")

        cadastrarForm = ClientForm(request.POST)
        if cadastrarForm.is_valid():
            name = cadastrarForm.cleaned_data['name']
            email = cadastrarForm.cleaned_data['email']
            password = cadastrarForm.cleaned_data['password']
            admin = cadastrarForm['admin']
            #Verificar se tem alguem já com esse nome
            if not User.objects.filter(username=name, email=email).exists():
                user = User.objects.create_user(username=name, email=email, password=password)
                login(request, user)
                if admin:
                    group, created = Group.objects.get_or_create(name='Administradores')
                    group.user_set.add(user)
                    return redirect("admin")
                else:
                    group, created = Group.objects.get_or_create(name='Usuarios')
                    group.user_set.add(user)
                    return redirect("dashboard")
            else:
                raise PermissionError("Nome já cadastrado")
    else:
        loginForm = ClientLoginForm()
        cadastrarForm = ClientForm()

    return render(request,'contact/login.html',{'login':loginForm, 'cadastrar':cadastrarForm})

@login_required(login_url='login/')
def Administrador(request):
    if not request.user.groups.filter(name='Administradores').exists():
        return redirect("dashboard")

    try:
        usuario_equipe = Client.objects.get(user=request.user).equipe
        membros_equipe = Client.objects.filter(equipe=usuario_equipe)
    except ObjectDoesNotExist:
        usuario_equipe, membros_equipe = False,False

    context = {
        'user': request.user,
        'equipe': usuario_equipe,
        'equipe_membros': membros_equipe,
    }
    return render(request,'contact/admin.html', context=context)

@login_required(login_url="login/")
def Dashboard(request):
    if request.method == 'POST':
        pass

    try:
        usuario_equipe = Client.objects.get(user=request.user).equipe
        membros_equipe = Client.objects.filter(equipe=usuario_equipe)
    except ObjectDoesNotExist:
        usuario_equipe, membros_equipe = False,False
   
    context = {
        'user': request.user,
        'equipe': usuario_equipe,
        'equipe_membros': membros_equipe,
    }
    return render(request, 'contact/dashboard.html', context=context)

@login_required(login_url="login/")
def UserLogout(request):
    logout(request)
    return redirect('login/')

