# Generated by Django 3.1.5 on 2021-07-08 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0043_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='date_of_publish',
        ),
    ]
