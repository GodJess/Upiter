# Generated by Django 4.2.3 on 2024-01-06 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_creditcard_debitcard_platinumcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
