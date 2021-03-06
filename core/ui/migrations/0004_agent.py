# Generated by Django 3.1.5 on 2021-01-13 16:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='FIRST NAME')),
                ('last_name', models.CharField(max_length=50, verbose_name='LAST NAME')),
                ('job', models.CharField(choices=[('Real Estate Broker', 'Real Estate Broker'), ('Real Estate Agent', 'Real Estate Agent')], default='Real Estate Broker', max_length=150, verbose_name='JOB')),
                ('img', models.ImageField(upload_to='', verbose_name='PICTURE')),
                ('phoneNumber', models.IntegerField(verbose_name='PHONE NUMBER')),
                ('email', models.EmailField(max_length=100, verbose_name='EMAIL ADRESS')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='FACBOOK ADRESS')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='TWITTER ADRESS')),
                ('google_plus', models.URLField(blank=True, null=True, verbose_name='GOOGLE PLUSE ADRESS')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='LINKEDNI ADRESS')),
                ('skypeid', models.CharField(blank=True, max_length=200, null=True, verbose_name='SKYPE ID')),
                ('inDate', models.DateField(auto_now_add=True, null=True, verbose_name='INDATE')),
                ('biography', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='BIOGRAPHY')),
                ('workExperience', models.IntegerField(blank=True, null=True, verbose_name='WORK EXPERIENCE')),
                ('experience', models.CharField(choices=[('years', 'years'), ('month', 'month')], default='years', max_length=150, verbose_name='EXPERIENCE')),
                ('status', models.BooleanField(default=True, verbose_name='to be seen ?')),
            ],
            options={
                'verbose_name_plural': 'AbOuT',
            },
        ),
    ]
