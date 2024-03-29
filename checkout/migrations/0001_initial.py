

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basket', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=150)),
                ('company_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('apartment', models.CharField(max_length=100)),
                ('town_city', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckoutBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cupon_code', models.CharField(blank=True, max_length=100, null=True)),
                ('is_checkout', models.BooleanField(default=False)),
                ('card_number', models.CharField(blank=True, max_length=20, null=True)),
                ('card_date', models.CharField(blank=True, max_length=5, null=True)),
                ('payment_type', models.CharField(choices=[('K', 'Karta'), ('N', 'Naxt')], max_length=1)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CheckoutBasket', to=settings.AUTH_USER_MODEL)),
                ('billing_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CheckoutBasket', to='checkout.billingdetails')),
                ('product_basket', models.ManyToManyField(related_name='product_basket', to='basket.productbasket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cupon_code', models.CharField(blank=True, max_length=100, null=True)),
                ('is_checkout', models.BooleanField(default=False)),
                ('card_number', models.CharField(blank=True, max_length=20, null=True)),
                ('card_date', models.CharField(blank=True, max_length=5, null=True)),
                ('payment_type', models.CharField(choices=[('K', 'Karta'), ('N', 'Naxt')], max_length=1)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('total_sum', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CheckoutProduct', to=settings.AUTH_USER_MODEL)),
                ('billing_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Checkoutbilling', to='checkout.billingdetails')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_checkout', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
