# Generated by Django 4.0.5 on 2022-07-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_group_manufacturer_person_topping_pizza_membership_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plant_name', models.CharField(max_length=50)),
                ('plant_category', models.CharField(default='00', max_length=20)),
                ('plant_subcategory', models.CharField(max_length=200)),
                ('plant_age', models.CharField(max_length=200)),
                ('plant_price', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('plant_image', models.ImageField(default='', upload_to='contacts/images')),
            ],
        ),
    ]
