# Generated by Django 5.0.1 on 2024-05-19 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpinghands', '0002_alter_donation_volunteer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='volunteermark',
            new_name='volunteerrmark',
        ),
    ]
