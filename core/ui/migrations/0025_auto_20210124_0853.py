# Generated by Django 3.1.5 on 2021-01-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0024_auto_20210122_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='inDate',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='ENTRY DATE'),
        ),
    ]
