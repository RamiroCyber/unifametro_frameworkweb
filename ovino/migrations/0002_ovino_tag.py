# Generated by Django 5.0.2 on 2024-02-24 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovino', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ovino',
            name='tag',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tag.tag'),
        ),
    ]
