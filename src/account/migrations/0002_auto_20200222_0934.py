# Generated by Django 3.0.3 on 2020-02-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first_name'),
        ),
    ]
