# Generated by Django 4.0.5 on 2022-07-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='', upload_to='contacts/images'),
        ),
    ]
