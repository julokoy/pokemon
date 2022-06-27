from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=150)
    height = models.IntegerField()
    weight = models.IntegerField()
    type = models.ForeignKey(
        "pokedex.PokemonType", related_name='types', on_delete=models.CASCADE,null=True
    )

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"
    
    def __str__(self):
        return self.name

class Stat(models.Model):
    name = models.CharField(max_length=100)
    effort = models.IntegerField()
    base_stat = models.IntegerField()
    pokemon = models.ForeignKey(Pokemon, related_name='stats', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Stat"
        verbose_name_plural = "Stats"
    
    def __str__(self):
        return self.name

class PokemonType(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "PokemonType"
        verbose_name_plural = "PokemonTypes"
    
    def __str__(self):
        return self.name
