# Generated by Django 3.1 on 2020-08-07 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='news_source',
            field=models.CharField(choices=[('1', '1')], default='bbc-news', max_length=50),
        ),
    ]
