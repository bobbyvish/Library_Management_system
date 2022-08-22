# Generated by Django 4.1 on 2022-08-22 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0001_initial'),
        ('Book', '0009_alter_transaction_amount_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Member.member'),
        ),
    ]