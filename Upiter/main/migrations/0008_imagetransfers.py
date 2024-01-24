# Generated by Django 4.2.3 on 2024-01-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_imagetransfer_alter_transfers_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTransfers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageUp', models.ImageField(upload_to='images/')),
                ('ImageDown', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'Картинки',
                'verbose_name_plural': 'Картинки',
            },
        ),
    ]