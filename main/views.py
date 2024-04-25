from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html') 

def check_age(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        if int(age) >= 18:
            return redirect('home')  # Rediriger vers la page d'accueil si l'âge est supérieur à 18
        else:
            return render(request, 'not_allowed.html')  # Afficher un message d'erreur si l'âge est inférieur à 18
    return render(request, 'check_age.html')
