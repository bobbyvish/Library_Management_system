# Generated by Django 4.1 on 2022-08-20 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_alter_book_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='count',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
