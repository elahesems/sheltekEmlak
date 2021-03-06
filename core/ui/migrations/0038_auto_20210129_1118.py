# Generated by Django 3.1.5 on 2021-01-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0037_auto_20210127_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='capacity',
            field=models.IntegerField(blank=True, null=True, verbose_name='capacity for Part Rent'),
        ),
        migrations.AlterField(
            model_name='house',
            name='type',
            field=models.CharField(choices=[('Rent', 'rent'), ('Sale', 'sale'), ('Part Rent', 'partRent')], default='rent', max_length=150),
        ),
    ]
