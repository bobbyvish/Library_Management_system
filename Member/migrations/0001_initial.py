# Generated by Django 4.1 on 2022-08-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=255)),
                ('member_email', models.EmailField(max_length=255)),
                ('registered_on', models.DateField(auto_now_add=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=11, null=True)),
                ('debt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=11, null=True)),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
