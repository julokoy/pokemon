from urllib.request import pathname2url
from django.urls import path
from pokedex import views
from django.views.generic import TemplateView

app_name = "pokedex"
urlpatterns = [
    path("", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("register/", views.Register.as_view(), name="register"),
    path("list/", views.PokemonList.as_view(), name="list"),
    path("list/stat", views.StatList.as_view(), name="stats"),
    path("details/<int:id>", views.PokemonDetail.as_view(), name="pokemon_details"),
    path("add-pokemon/", views.AddPokemon.as_view(), name="add_pokemon"),
    path("update-pokemon/<int:id>", views.UpdatePokemon.as_view(), name="update_pokemon"),
    path("delete-pokemon/<int:id>", views.DeletePokemon.as_view(), name="delete_pokemon"),
    path(
        "details/stats/<int:id>/", views.StatDetail.as_view(), name="display_stats"
    ),
    path("search-pokemon/", views.SearchPokemon.as_view(), name="search_pokemon"),
    path("filter-pokemon/", views.FilterPokemon.as_view(), name="filter_pokemon"),
]
