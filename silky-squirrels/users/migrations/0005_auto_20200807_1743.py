# Generated by Django 3.0.8 on 2020-08-08 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0004_profile_background")]

    operations = [
        migrations.AlterField(model_name="profile", name="background", field=models.ImageField(upload_to="background"))
    ]
