# Generated by Django 3.2 on 2021-09-27 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('total_toll_milles', models.FloatField(default=0.0)),
                ('total_non_toll_milles', models.FloatField(default=0.0)),
                ('total_gallons', models.FloatField(default=0.0)),
                ('total_taxes', models.FloatField(default=0.0)),
                ('total_mpg', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='StateTaxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('initials', models.CharField(max_length=256)),
                ('number', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('tax', models.FloatField(default=0.0)),
                ('fuel', models.CharField(default='Biodiesel', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=256)),
                ('nickname', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='StateReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('initials', models.CharField(max_length=256)),
                ('total_toll_milles', models.FloatField(default=0.0)),
                ('total_non_toll_milles', models.FloatField(default=0.0)),
                ('total_gallons', models.FloatField(default=0.0)),
                ('total_taxes', models.FloatField(default=0.0)),
                ('total_mpg', models.FloatField(default=0.0)),
                ('quarter', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='truck_management_app.quarter')),
            ],
        ),
        migrations.AddField(
            model_name='quarter',
            name='truck',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='truck_management_app.truck'),
        ),
    ]
