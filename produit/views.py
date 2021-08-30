from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Produit
from .forms import FormulaireAjoutProduit

# Create your views here.
@login_required(login_url='access')
def index(request):
    produits = Produit.objects.all()
    context = {'produits': produits}
    return render(request, 'produit/accueil.html', context)

@login_required(login_url='access')
def ajouter(request):
    form=FormulaireAjoutProduit()  
    if request.method=='POST':
        form=FormulaireAjoutProduit(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'produit/ajouter.html',context)

@login_required(login_url='access')
def modifier(request,pk):
    produit=Produit.objects.get(id=pk)
    form=FormulaireAjoutProduit(instance=produit)
    if request.method=='POST':
        form=FormulaireAjoutProduit(request.POST,instance=produit)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'produit/modifier.html',context)
