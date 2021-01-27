# Generated by Django 3.1.5 on 2021-01-25 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0026_auto_20210124_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='homeName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.house', verbose_name='House Name'),
        ),
        migrations.CreateModel(
            name='CtrlComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='to be seen ??')),
                ('homeName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.house', verbose_name='')),
            ],
        ),
    ]