# Generated by Django 2.2.6 on 2019-10-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisapp', '0002_auto_20191014_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='account_name',
            field=models.CharField(default='Survey', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='bank_name',
            field=models.CharField(default='StanbicIBTC', max_length=50),
            preserve_default=False,
        ),
    ]