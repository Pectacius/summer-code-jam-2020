# Generated by Django 3.0.8 on 2020-08-04 05:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='user',
            field=models.ForeignKey(default=0, on_delete=models.SET('Deleted'), to=settings.AUTH_USER_MODEL,
                                    to_field='username'),
            preserve_default=False,
        ),
    ]
