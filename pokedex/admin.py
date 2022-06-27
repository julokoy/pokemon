from django.contrib import admin

from .models import Pokemon, Stat, PokemonType

class PokemonAdmin(admin.ModelAdmin):
    fields = ["id", "name", "height", "weight", "type"]
    search_fields = ["name"]

class PokemonTypeAdmin(admin.ModelAdmin):
    fields = ["name"]
    search_fields = ["name"]


admin.site.register(Stat)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonType, PokemonTypeAdmin)