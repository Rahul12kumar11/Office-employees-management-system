# Generated by Django 3.2.9 on 2022-02-09 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='department',
            table='department',
        ),
        migrations.AlterModelTable(
            name='role',
            table='role',
        ),
    ]