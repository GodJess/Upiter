# Generated by Django 4.2.3 on 2024-01-03 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='User Name')),
                ('surname', models.CharField(max_length=100, verbose_name='User lname')),
                ('phone', models.CharField(max_length=100, verbose_name='User phone')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100, verbose_name='User password')),
                ('photo', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
