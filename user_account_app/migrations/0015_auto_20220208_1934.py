# Generated by Django 3.2 on 2022-02-08 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account_app', '0014_auto_20220207_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='driver_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='driver_phone',
            new_name='phone',
        ),
    ]
