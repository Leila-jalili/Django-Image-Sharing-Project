# Generated by Django 3.2 on 2021-04-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='summary',
            field=models.TextField(default='Summary'),
        ),
    ]
