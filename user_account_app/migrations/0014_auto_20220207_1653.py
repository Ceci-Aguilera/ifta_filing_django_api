# Generated by Django 3.2 on 2022-02-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account_app', '0013_alter_user_occupation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=256)),
                ('last_name', models.CharField(default='', max_length=256)),
                ('password', models.CharField(default='-1', max_length=50)),
                ('driver_email', models.EmailField(default='', max_length=256, unique=True)),
                ('driver_phone', models.CharField(default='', max_length=20, unique=True, verbose_name='phone')),
                ('last_uid', models.CharField(default='-1', max_length=256)),
                ('last_token', models.CharField(default='-1', max_length=256)),
                ('last_uid_password', models.CharField(default='-1', max_length=256)),
                ('last_token_password', models.CharField(default='-1', max_length=256)),
                ('zip_code', models.CharField(default='', max_length=256)),
                ('usa_state', models.CharField(default='', max_length=256)),
                ('ocupation', models.CharField(choices=[('COMPANY OWNER', 'COMPANY OWNER'), ('FLEET MANAGER', 'FLEET MANAGER'), ('DRIVER', 'DRIVER')], default='DRIVER', max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='accountcategory',
            name='max_amount_of_drivers',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='drivers',
            field=models.ManyToManyField(related_name='company_owners', to='user_account_app.Driver'),
        ),
    ]
