# Generated by Django 3.1.4 on 2020-12-29 22:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_auto_20201217_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='CustomerUser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 31, 22, 30, 45, 330782, tzinfo=utc)),
        ),
    ]
