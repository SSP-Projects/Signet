# Generated by Django 3.2 on 2021-04-15 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_management', '0002_auto_20210415_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='center_id',
            field=models.UUIDField(choices=[], verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='centers', verbose_name='Center ID')),
        ),
    ]
