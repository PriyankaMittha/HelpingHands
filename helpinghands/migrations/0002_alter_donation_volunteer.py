# Generated by Django 5.0.1 on 2024-05-05 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpinghands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='volunteer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpinghands.volunteer'),
        ),
    ]
