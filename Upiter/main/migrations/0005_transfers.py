# Generated by Django 4.2.3 on 2024-01-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_transfer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sender', models.CharField(max_length=100, verbose_name='Отправитель')),
                ('Recipient', models.CharField(max_length=100, verbose_name='Получатель')),
                ('WhereFrom', models.CharField(max_length=100, verbose_name='Счет списания')),
                ('Where', models.CharField(max_length=100, verbose_name='Счет пополнения')),
                ('Date', models.DateField(verbose_name='Дата отправки')),
                ('Time', models.TimeField(verbose_name='Время отправки')),
                ('Summ', models.CharField(max_length=100, verbose_name='Сумма транзакции')),
                ('CardNameOfDepozit', models.CharField(max_length=100, verbose_name='Название карты пополнения')),
                ('CardNameOffs', models.CharField(max_length=100, verbose_name='Название карты списания')),
                ('SenderSurname', models.CharField(max_length=100, verbose_name='Отправитель_фамилия')),
                ('RecipientSurname', models.CharField(max_length=100, verbose_name='Получатель_фамилия')),
            ],
            options={
                'verbose_name': 'Перевод',
                'verbose_name_plural': 'Транзакции',
            },
        ),
    ]
