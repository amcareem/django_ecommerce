# Generated by Django 5.0 on 2023-12-30 19:43

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('about', models.CharField(blank=True, max_length=500, null=True)),
                ('item_type_keywords', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '1. Item Types',
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('value_in_kg', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '3. Weight Groups',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('address_line_1', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('gst_number', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_number', models.CharField(max_length=10)),
                ('delivery_instructions', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_default', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '4. Address/Billing Informations',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('contact_name', models.CharField(max_length=100, null=True)),
                ('contact_number', models.CharField(max_length=10, null=True)),
                ('max_quantity', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.address')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('weight_group', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.weight')),
            ],
            options={
                'verbose_name_plural': '5. Inventories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('about', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('item_keywords', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.itemtype')),
            ],
            options={
                'verbose_name_plural': '2. Items',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('original_price_per_quantity', models.PositiveIntegerField(default=1)),
                ('selling_price_per_quantity', models.PositiveIntegerField(default=1)),
                ('minimum_order_quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], max_length=200, null=True)),
                ('about', models.CharField(blank=True, max_length=500, null=True)),
                ('keywords', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('inventory_name', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.inventory')),
                ('item_type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.item')),
                ('weight_group', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.weight')),
            ],
            options={
                'verbose_name_plural': '6. Listings',
            },
        ),
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, null=True)),
                ('invoice_id', models.CharField(max_length=100, null=True)),
                ('GST_applicable', models.BooleanField(default=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('is_igst', models.BooleanField(default=False)),
                ('rebate', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('cgst', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('sgst', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('igst', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('purchase_price_per_quantity', models.PositiveIntegerField(default=1)),
                ('total_price', models.PositiveIntegerField(default=1)),
                ('order_status', models.CharField(choices=[('PLACED', 'Placed'), ('ACCEPTED', 'Accepted'), ('PACKED', 'Packed'), ('SHIPPED', 'Shipped'), ('REJECTED', 'Rejected'), ('COMPLETED', 'Completed')], max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('inventory_name', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.inventory')),
                ('item_name', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.listing')),
                ('weight_group', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.weight')),
            ],
            options={
                'verbose_name_plural': '7. Ordered Items',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, null=True, unique=True)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('To Pay', 'To Pay'), ('Failed', 'Failed')], max_length=200, null=True)),
                ('payment_mode', models.CharField(choices=[('Cash', 'Cash'), ('NEFT', 'NEFT'), ('RTGS', 'RTGS'), ('Cheque', 'Cheque'), ('Payment Gateway', 'Payment Gateway')], max_length=200, null=True)),
                ('payment_details', models.CharField(blank=True, max_length=200, null=True)),
                ('total_price', models.PositiveIntegerField(default=1)),
                ('grand_total', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('billing_address', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='billing', to='genesis.address')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('shipping_address', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='shipping', to='genesis.address')),
                ('item_details', models.ManyToManyField(to='genesis.ordereditems')),
            ],
            options={
                'verbose_name_plural': '8. Order/Transactions',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('seller_action_required', models.BooleanField(default=True)),
                ('buyer_action_required', models.BooleanField(default=False)),
                ('po_file', models.FileField(blank=True, upload_to='documents/po/')),
                ('quote_file', models.FileField(blank=True, upload_to='documents/qo/')),
                ('invoice_file', models.FileField(blank=True, upload_to='documents/in/')),
                ('delivery_receipt_file', models.FileField(blank=True, upload_to='documents/dr/')),
                ('status', models.CharField(blank=True, choices=[('QUOTE_SENT', 'Quote Sent'), ('PURCHASE_ORDER_SENT', 'Purchase Order Sent'), ('RECEIVED', 'Quote Request Received'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('billing_address', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.address')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('item_name', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.listing')),
                ('weight_group', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='genesis.weight')),
            ],
            options={
                'verbose_name_plural': '9. Request Quotes',
            },
        ),
    ]
