# Generated by Django 3.1.1 on 2020-11-11 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]