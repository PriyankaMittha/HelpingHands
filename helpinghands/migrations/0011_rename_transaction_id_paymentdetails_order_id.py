# Generated by Django 5.0.1 on 2024-05-26 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpinghands', '0010_rename_order_id_paymentdetails_transaction_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='transaction_id',
            new_name='order_id',
        ),
    ]
