# Generated by Django 5.0.1 on 2024-05-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpinghands', '0005_rename_donationarea_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
