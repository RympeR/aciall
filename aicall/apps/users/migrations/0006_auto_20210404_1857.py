# Generated by Django 3.1.7 on 2021-04-04 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210330_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='reciever_name',
            field=models.CharField(default='1617562510.993363', max_length=100, verbose_name='Characterisric sender name'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 0, 20), verbose_name='Expires at'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='test', max_length=150, verbose_name='first name'),
            preserve_default=False,
        ),
    ]