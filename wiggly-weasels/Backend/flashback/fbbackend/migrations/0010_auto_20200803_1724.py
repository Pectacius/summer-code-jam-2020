# Generated by Django 3.0.8 on 2020-08-03 17:24

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbbackend', '0009_auto_20200802_1951'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.RemoveField(
            model_name='account',
            name='identification',
        ),
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.RemoveField(
            model_name='group',
            name='identification',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='nickname',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='messages',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), size=None),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='identification',
            field=models.CharField(blank=True, default='0d1ff0fcd2db45ec815205cb42e90695', max_length=100, primary_key=True, serialize=False),
        ),
    ]
