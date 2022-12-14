# Generated by Django 4.1 on 2022-08-21 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0001_initial'),
        ('Book', '0005_alter_book_author_alter_book_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(null=True)),
                ('total_days', models.IntegerField(null=True)),
                ('total_charge', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Book.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Member.member')),
            ],
            options={
                'db_table': 'transaction',
            },
        ),
    ]
