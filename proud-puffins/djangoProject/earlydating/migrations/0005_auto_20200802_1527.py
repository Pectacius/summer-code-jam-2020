# Generated by Django 3.0.8 on 2020-08-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earlydating', '0004_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(null=True, upload_to='static/user_pixel'),
        ),
    ]
