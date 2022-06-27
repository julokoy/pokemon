from django.shortcuts import render, redirect
import requests
from .models import Pokemon, Stat
from .forms import DeletePokemonForm, StatDetailForm, StatListForm, PokemonDetailForm, PokemonForm, UpdatePokemonForm, PokemonListForm
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class PokemonList(View):
    form_class = PokemonListForm
    initial = {"key": "value"}
    template_name = "pokedex/display_pokemon.html"

    def get(self, request, *args, **kwargs):
        pokemons = Pokemon.objects.all()
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"pokemons": pokemons})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("pokedex:display_pokemon"))

        return render(request, self.template_name, {"form": form})

class StatList(View):
    form_class = StatListForm
    initial = {"key": "value"}
    template_name = "pokedex/display_allstats.html"

    def get(self, request, *args, **kwargs):
        stats = Stat.objects.all()
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"stats": stats})

class PokemonDetail(View):
    form_class = PokemonDetailForm
    initial = {"key": "value"}
    template_name = "pokedex/display_details.html"

    def get(self, request, id, *args, **kwargs):
        pokemons = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"details": pokemons})

class AddPokemon(View):
    form_class = PokemonForm
    initial = {"key": "value"}
    template_name = "pokedex/add_pokemon.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("pokedex:add_pokemon"))

        return render(request, self.template_name, {"form": form})

class UpdatePokemon(View):
    form_class = UpdatePokemonForm
    initial = {"key": "value"}
    template_name = "pokedex/update_pokemon.html"

    def get(self, request, id, *args, **kwargs):
        pokemon_id = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial, instance = pokemon_id) 
        return render(request, self.template_name, {"form": form})

    def post(self, request, id, *args, **kwargs):
        pokemon_id = Pokemon.objects.get(id=id)
        form = self.form_class(request.POST, instance=pokemon_id)
        if form.is_valid():
            form.save()
            return redirect("pokedex:update_pokemon", pokemon_id.id)

        return render(request, self.template_name, {"form": form})

class DeletePokemon(View):
    form_class = DeletePokemonForm
    initial = {"key": "value"}
    template_name = "pokedex/delete_pokemon.html"

    def get(self, request, id, *args, **kwargs):
        pokemon_id = Pokemon.objects.get(id=id)
        form = self.form_class(initial=self.initial, instance = pokemon_id) 
        return render(request, self.template_name, {"form": form})

    def post(self, request, id, *args, **kwargs):
        pokemon_id = Pokemon.objects.get(id=id)
        form = self.form_class(request.POST, instance=pokemon_id)
        if form.is_valid():
            pokemon_id.delete()
            return HttpResponseRedirect(reverse("pokedex:list"))

        return render(request, self.template_name, {"form": form})

class StatDetail(View):
    form_class = StatDetailForm
    initial = {"key": "value"}
    template_name = "pokedex/display_stats.html"

    def get(self, request, id, *args, **kwargs):
        stats = Stat.objects.get(id=id)
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"stats": stats})

class SearchPokemon(View):
    form_class = PokemonForm
    initial = {"key": "value"}
    template_name = "pokedex/search_pokemon.html"

    def get(self, request, *args, **kwargs):
        error = False
        if "q" in request.GET:
            q = request.GET["q"]
            if not q:
                error = True
            else:
                pokemons = Pokemon.objects.filter(name__icontains=q)
                return render(
                    request,
                    "pokedex/search_pokemon_result.html",
                    {"pokemons": pokemons, "query": q},
                )
        return render(request, self.template_name, {"error": error})

class FilterPokemon(View):
    form_class = PokemonForm
    initial = {"key": "value"}
    template_name = "pokedex/filter_pokemon.html"

    def get(self, request, *args, **kwargs):
        error = False
        if "q" in request.GET:
            q = request.GET["q"]
            if not q:
                error = True
            else:
                pokemons = Pokemon.objects.filter(type__name__icontains=q)
                return render(
                    request,
                    "pokedex/filter_pokemon_result.html",
                    {"pokemons": pokemons, "query": q},
                )
        return render(request, self.template_name, {"error": error})
