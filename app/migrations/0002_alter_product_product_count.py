# Generated by Django 4.1.5 on 2023-01-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_count',
            field=models.IntegerField(),
        ),
    ]
