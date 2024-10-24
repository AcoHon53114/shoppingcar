# Generated by Django 4.2 on 2024-10-07 04:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_id', models.IntegerField(default=4)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('braintree_id', models.CharField(blank=True, max_length=150)),
                ('username', models.CharField(blank=True, default='', max_length=150)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_id', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('studio_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('booking_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('guests', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('lasting_hours', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('product_desc', models.TextField(blank=True, default='', max_length=200)),
                ('username', models.CharField(blank=True, default='', max_length=150)),
                ('related_order_id', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.product')),
            ],
        ),
    ]
