# Generated by Django 3.2 on 2021-04-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_taxis_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxis',
            name='emile',
            field=models.EmailField(max_length=255),
        ),
    ]