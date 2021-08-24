# Generated by Django 3.1.1 on 2020-10-27 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='price')),
                ('price_bill', models.CharField(max_length=3, verbose_name='price bill')),
                ('unit', models.CharField(max_length=10, verbose_name='unit')),
                ('price_unit', models.CharField(max_length=10, verbose_name='price unit')),
                ('img', models.ImageField(blank=True, upload_to='', verbose_name='img')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('short_description', models.TextField(blank=True, max_length=110, verbose_name='Short description')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.productcategory')),
            ],
        ),
    ]