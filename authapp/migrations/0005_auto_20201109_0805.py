# Generated by Django 3.1.1 on 2020-11-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_address_intercom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='floor',
            field=models.IntegerField(blank=True, max_length=3, null=True, verbose_name='Этаж'),
        ),
    ]