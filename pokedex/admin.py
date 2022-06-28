from django.contrib import admin

from .models import Pokemon, Stat, PokemonType

class PokemonAdmin(admin.ModelAdmin):
    list_display = ["name", "height", "weight", "type"]
    search_fields = ["name"]

class PokemonTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

class PokemonStatsAdmin(admin.ModelAdmin):
    list_display = ["name", "effort", "base_stat", "pokemon"]
    search_fields = ["name"]


admin.site.register(Stat, PokemonStatsAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonType, PokemonTypeAdmin)