# Generated by Django 3.0.5 on 2023-01-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshopping', '0002_rename_place_table1_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
