# Generated by Django 3.0.3 on 2020-03-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='email',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='room_name',
        ),
        migrations.AddField(
            model_name='chat',
            name='content',
            field=models.CharField(default='Null', max_length=50),
        ),
    ]