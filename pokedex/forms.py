from pokedex.models import Stat, Pokemon
from django import forms

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"

class PokemonListForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"

class PokemonDetailForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"

class StatListForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = "__all__"

class StatDetailForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = "__all__"

class UpdatePokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ["name", "height", "weight", "type"]

class DeletePokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ["name", "height", "weight", "type"]