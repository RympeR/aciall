# Generated by Django 3.1.7 on 2021-03-24 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20210324_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talkthemes',
            name='image_svg',
            field=models.FloatField(blank=True, null=True, verbose_name='ImageSVG'),
        ),
    ]