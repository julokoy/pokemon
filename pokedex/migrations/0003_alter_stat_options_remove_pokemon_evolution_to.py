# Generated by Django 4.0.5 on 2022-06-27 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_alter_pokemon_options_alter_pokemon_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stat',
            options={'verbose_name': 'Stat', 'verbose_name_plural': 'Stats'},
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='evolution_to',
        ),
    ]
