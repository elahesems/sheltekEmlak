# Generated by Django 3.1.5 on 2021-01-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0016_auto_20210117_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='PICTURE1'),
        ),
        migrations.AddField(
            model_name='house',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='PICTURE2'),
        ),
        migrations.AddField(
            model_name='house',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='PICTURE3'),
        ),
        migrations.AddField(
            model_name='house',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='PICTURE4'),
        ),
        migrations.AddField(
            model_name='house',
            name='imgAppearance',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='PICTURE APPEARANCE'),
        ),
        migrations.DeleteModel(
            name='Pictures',
        ),
    ]