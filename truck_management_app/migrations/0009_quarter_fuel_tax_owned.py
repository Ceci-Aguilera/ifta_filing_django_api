# Generated by Django 3.2 on 2022-02-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck_management_app', '0008_rename_total_mpg_statereport_fuel_tax_owned'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarter',
            name='fuel_tax_owned',
            field=models.FloatField(default=0.0),
        ),
    ]
