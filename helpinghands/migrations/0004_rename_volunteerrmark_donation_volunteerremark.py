# Generated by Django 5.0.1 on 2024-05-19 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpinghands', '0003_rename_volunteermark_donation_volunteerrmark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='volunteerrmark',
            new_name='volunteerremark',
        ),
    ]
