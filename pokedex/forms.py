from pokedex.models import Stat, Pokemon
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class PokemonLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class PokemonRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["first_name", "last_name", "username", "email"]

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