# Generated by Django 3.2.3 on 2021-06-23 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('genesis', '0030_alter_order_grand_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('seller_action_required', models.BooleanField(default=True)),
                ('buyer_action_required', models.BooleanField(default=False)),
                ('po_file', models.FileField(upload_to='documents/')),
                ('quote_file', models.FileField(upload_to='documents/')),
                ('status', models.CharField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('item_name', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.listing')),
            ],
            options={
                'verbose_name_plural': '9. Request Quotes',
            },
        ),
    ]
