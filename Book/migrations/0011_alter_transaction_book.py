# Generated by Django 4.1 on 2022-08-22 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0010_alter_book_quantity_alter_transaction_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.book'),
        ),
    ]
