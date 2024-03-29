# Generated by Django 4.0.5 on 2022-07-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_plant_plant_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_name',
            field=models.CharField(choices=[('Money tree (Pachira aquatica)', 'Money tree (Pachira aquatica)'), ('Fiddle leaf fig (Ficus lyrata)', 'Fiddle leaf fig (Ficus lyrata)'), ('Rubber plant (Ficus elastica)', 'Rubber plant (Ficus elastica)'), ('Giant bird of paradise (Strelitzia nicolai)', 'Giant bird of paradise (Strelitzia nicolai)'), ('Monstera (Monstera deliciosa)', 'Monstera (Monstera deliciosa)')], default='', max_length=50),
        ),
    ]
