# Generated by Django 3.2.3 on 2021-06-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genesis', '0031_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='delivery_receipt_file',
            field=models.FileField(blank=True, upload_to='documents/dr/'),
        ),
        migrations.AddField(
            model_name='quote',
            name='invoice_file',
            field=models.FileField(blank=True, upload_to='documents/in/'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='po_file',
            field=models.FileField(blank=True, upload_to='documents/po/'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote_file',
            field=models.FileField(blank=True, upload_to='documents/qo/'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='status',
            field=models.CharField(blank=True, choices=[('QUOTE_SENT', 'Quote Sent'), ('PURCHASE_ORDER_SENT', 'Purchase Order Sent'), ('RECEIVED', 'Quote Request Received'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], max_length=50, null=True),
        ),
    ]
