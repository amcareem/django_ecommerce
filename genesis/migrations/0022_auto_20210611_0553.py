# Generated by Django 3.2.3 on 2021-06-11 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genesis', '0021_auto_20210611_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereditems',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ordereditems',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='ordereditems',
            name='updated_at',
        ),
    ]
