# Generated by Django 4.0.5 on 2022-07-13 13:31

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_mobile_alter_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='https://i0.wp.com/www.grihshobha.in/wp-content/uploads/2019/12/apna.jpg?fit=1024%2C680&ssl=1', upload_to=home.models.upload_image),
        ),
    ]
