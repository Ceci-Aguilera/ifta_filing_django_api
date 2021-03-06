# Generated by Django 3.2 on 2021-10-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account_app', '0009_auto_20211003_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverprofile',
            name='email',
            field=models.EmailField(default='', max_length=256, unique=True),
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='password',
            field=models.CharField(default='-1', max_length=50),
        ),
        migrations.AlterField(
            model_name='driverprofile',
            name='phone',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='phone'),
        ),
    ]
