from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Commande
from .forms import FormulaireAjoutCommande

# Create your views here.

@login_required(login_url='access')
def index(request):
    return HttpResponse('<h1>commande</h1>')

@login_required(login_url='access')
def listing(request):
    commandes=Commande.objects.all()
    context={'commandes':commandes}
    return render(request,'commande/list_commande.html',context)



@login_required(login_url='access')
def ajouter(request):
    form=FormulaireAjoutCommande()  
    if request.method=='POST':
        form=FormulaireAjoutCommande(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/commande/listing/')
    context={'form':form}
    return render(request,'commande/ajouter_commande.html',context)

@login_required(login_url='access')
def modifier(request,pk):
    commande=Commande.objects.get(id=pk)
    form=FormulaireAjoutCommande(instance=commande)  
    if request.method=='POST':
        form=FormulaireAjoutCommande(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/commande/listing/')
    context={'form':form}
    return render(request,'commande/modifier_commande.html',context)

@login_required(login_url='access')
def supprimer(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method=='POST':
        commande.delete()
        return redirect('/commande/listing/')

    context={'item':commande}
    return render(request,'commande/supprimer_commande.html',context)