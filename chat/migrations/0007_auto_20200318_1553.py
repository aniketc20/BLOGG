# Generated by Django 3.0.3 on 2020-03-18 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0006_auto_20200316_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='author_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]