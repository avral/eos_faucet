# Generated by Django 2.0.7 on 2018-07-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faucet', '0002_account_is_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
