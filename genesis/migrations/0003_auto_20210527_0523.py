# Generated by Django 3.2.3 on 2021-05-27 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genesis', '0002_quicknotifications_userchats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='location',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='pincode',
        ),
        migrations.AddField(
            model_name='address',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='address',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='genesis.address'),
        ),
    ]
