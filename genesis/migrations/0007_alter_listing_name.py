# Generated by Django 3.2.3 on 2021-05-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genesis', '0006_auto_20210527_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]