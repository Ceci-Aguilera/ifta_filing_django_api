# Generated by Django 3.2 on 2022-02-19 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck_management_app', '0007_newentry_current_quarter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statereport',
            old_name='total_mpg',
            new_name='fuel_tax_owned',
        ),
    ]
