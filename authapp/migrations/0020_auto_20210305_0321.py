# Generated by Django 3.1.6 on 2021-03-05 00:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0019_auto_20210303_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 7, 0, 21, 34, 488926, tzinfo=utc)),
        ),
    ]
