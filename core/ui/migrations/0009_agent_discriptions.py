# Generated by Django 3.1.5 on 2021-01-16 13:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0008_auto_20210116_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='discriptions',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
