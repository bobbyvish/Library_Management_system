# Generated by Django 4.1 on 2022-08-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0007_book_book_stock_book_rented'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='total_days',
            field=models.IntegerField(default=0),
        ),
    ]
