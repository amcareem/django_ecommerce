# Generated by Django 3.2.3 on 2021-06-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genesis', '0013_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
