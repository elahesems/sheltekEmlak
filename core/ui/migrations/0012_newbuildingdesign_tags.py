# Generated by Django 3.1.5 on 2021-01-17 06:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0011_newbuildingdesign_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='newbuildingdesign',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('duplex', 'duplex'), ('villa', 'villa'), ('apartment', 'apartment'), ('commercial', 'commercial'), ('building', 'building'), ('realEstate', 'realEstate')], max_length=53, null=True),
        ),
    ]
