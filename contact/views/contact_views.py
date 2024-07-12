from django.shortcuts import render
from contact.forms import ClientForm

def index(request):
    return render(request,'contact/index.html')


def login(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dashboard")
    else:
        form = ClientForm()

    return render(request,'contact/login.html',{'form': form})
