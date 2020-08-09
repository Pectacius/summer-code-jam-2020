# Generated by Django 3.0.8 on 2020-08-09 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20200804_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('volume', models.IntegerField()),
                ('ticker_symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('volume', models.IntegerField()),
                ('ticker_symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.Stock')),
            ],
        ),
    ]
