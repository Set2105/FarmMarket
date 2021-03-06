# Generated by Django 3.1.4 on 2020-12-30 01:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_auto_20201230_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='CustomerUser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 1, 23, 24, 388820, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='CustomerUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_line', models.CharField(blank=True, max_length=128, verbose_name='теги')),
                ('about_me', models.TextField(blank=True, max_length=512, verbose_name='о себе')),
                ('gender', models.CharField(choices=[('M', 'М'), ('F', 'Ж')], max_length=1, verbose_name='пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
