# Generated by Django 3.1.7 on 2021-03-30 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20210324_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='NegativeSide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=255, verbose_name='Negative side ru')),
                ('name_eng', models.CharField(max_length=255, verbose_name='Negative side eng')),
            ],
        ),
        migrations.CreateModel(
            name='PositiveSide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=255, verbose_name='Positive side ru')),
                ('name_eng', models.CharField(max_length=255, verbose_name='Positive side eng')),
            ],
        ),
        migrations.AlterField(
            model_name='talkthemes',
            name='image_svg',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='ImageSVG'),
        ),
    ]