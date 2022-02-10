# Generated by Django 3.2.9 on 2022-02-09 18:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220209_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='details',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='details',
            field=models.CharField(default=datetime.datetime(2022, 2, 9, 18, 55, 41, 512245, tzinfo=utc), max_length=400),
            preserve_default=False,
        ),
    ]