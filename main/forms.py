from django import forms

class GraphiqueForm(forms.Form):
    ticker = forms.CharField(label='Nom de l\'action (ticker)', max_length=10)
    date_debut = forms.DateField(label='Date de début')
    date_fin = forms.DateField(label='Date de fin')
    type_graphique = forms.ChoiceField(label='Type de graphique', choices=[('line', 'Ligne'), ('candlestick', 'Chandelier')])
