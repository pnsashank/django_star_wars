# Generated by Django 2.1 on 2019-12-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planets', '0002_auto_20191226_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='films',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='gravity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='orbital_period',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='rotation_period',
            field=models.CharField(max_length=100, null=True),
        ),
    ]