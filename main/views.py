from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GraphiqueForm
from .utils import afficher_graphique_action

@login_required
def home(request):
    if request.method == 'POST':
        form = GraphiqueForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            date_debut = form.cleaned_data['date_debut']
            date_fin = form.cleaned_data['date_fin']
            type_graphique = form.cleaned_data['type_graphique']
            afficher_graphique_action(ticker, date_debut, date_fin, type_graphique)
            return redirect('home')  # Redirection vers la page d'accueil après avoir affiché le graphique
    else:
        form = GraphiqueForm()
    return render(request, 'home.html', {'form': form})

def not_allowed(request):
    return render(request, 'not_allowed.html')

def check_age(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        if int(age) >= 18:
            return redirect('home')
        else:
            return redirect('not_allowed')
    return render(request, 'check_age.html')

def graphique(request):
    # Votre logique de vue pour la page graphique ici
    pass