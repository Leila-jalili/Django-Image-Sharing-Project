# Generated by Django 3.2 on 2021-04-08 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_summary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
