from django import forms

class CrearPokemonForm(forms.Form):
    IDpoke = forms.IntegerField(label='ID Pokemon')
    Descripcion = forms.CharField(label='Descripcion Pokemon')
    Peso = forms.DecimalField(label='Peso (Kg)', min_value=20.0)
    Altura = forms.DecimalField(label='Altura (M)', min_value=20.0)

