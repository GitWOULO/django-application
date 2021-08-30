from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreationUtilisateur
from django.contrib.auth.decorators import login_required

# Create your views here.

def inscription(request):
    form=CreationUtilisateur()
    if request.method=='POST':        
        form=CreationUtilisateur(request.POST)         
        if form.is_valid():            
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Compte créé avec succès')
            return redirect('/')
    context={'form':form}
    return render(request,'compte/inscription.html',context)


@login_required(login_url='access')
def access(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Utilisateur ou mot de passe incorrect')
    return render(request,'compte/access.html',context)

@login_required(login_url='access')
def logoutUser(request):
    logout(request)
    return redirect('access')