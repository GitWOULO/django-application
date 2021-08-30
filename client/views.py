import commande
from django.contrib.auth.decorators import login_required
import client
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Client
from commande.models import Commande
from .forms import FormulaireAjoutClient
from commande.filters import CommandeFilter

# Create your views here.
@login_required(login_url='access')
def index(request):
    return HttpResponse('<h1>client</h1>')


@login_required(login_url='access')
def listing(request):
    clients=Client.objects.all()
    commandes=Commande.objects.all()
    contex={'clients':clients,'commandes':commandes}
    return render(request,'client/list_client.html',contex)

@login_required(login_url='access')
def profil_client(request,pk):
    client=Client.objects.get(id=pk)
    commandes=client.commande_set.all()    
    nombre_commande=commandes.count()
    myFilter=CommandeFilter(request.GET,queryset=commandes)
    commandes= myFilter.qs

    context={'client':client,'commandes':commandes,'nombre_commande':nombre_commande,'myFilter':myFilter}
    return render(request,'client/profil_client.html',context)

@login_required(login_url='access')
def supprimer_client(request,pk):
    client=Client.objects.get(id=pk)
    if request.method=='POST':
        client.delete()
        return redirect('/client/listing')
    context={'item':client}
    return render(request,'client/supprimer_client.html',context)

@login_required(login_url='access')
def creer_client(request):
    form=FormulaireAjoutClient()
    if request.method=='POST':                      
        form=FormulaireAjoutClient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/client/listing/')
    context={'form':form}
    return render(request,'client/creer_client.html',context)

@login_required(login_url='access')
def modifier_client(request,pk):
    client=Client.objects.get(id=pk)
    form=FormulaireAjoutClient(instance=client)
    if request.method=='POST':
        form=FormulaireAjoutClient(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('/client/profil/'+str(pk))
    context={'form':form, 'client':client}
    return render(request,'client/modifier_client.html',context)