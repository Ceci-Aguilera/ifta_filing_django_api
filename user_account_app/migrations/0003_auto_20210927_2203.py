# Generated by Django 3.2 on 2021-09-27 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_account_app', '0002_auto_20210926_2045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountcategory',
            options={'verbose_name_plural': 'account categories'},
        ),
        migrations.AddField(
            model_name='accountcategory',
            name='max_amount_of_drivers',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='company_name',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='phone')),
                ('last_uid', models.CharField(default='-1', max_length=256)),
                ('last_token', models.CharField(default='-1', max_length=256)),
                ('last_uid_password', models.CharField(default='-1', max_length=256)),
                ('last_token_password', models.CharField(default='-1', max_length=256)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
