# Generated by Django 3.2.3 on 2021-05-28 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genesis', '0008_order_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchats',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='userchats',
            name='created_for',
        ),
        migrations.DeleteModel(
            name='QuickNotifications',
        ),
        migrations.DeleteModel(
            name='UserChats',
        ),
    ]