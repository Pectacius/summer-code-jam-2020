# Generated by Django 3.0.9 on 2020-08-06 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifapp', '0003_auto_20200805_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='animation_position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
