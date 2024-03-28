# Generated by Django 5.0.3 on 2024-03-28 12:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0007_remove_basket_product_basket'),
        ('checkout', '0001_initial'),
        ('products', '0007_rename_name_color_color_rename_name_size_size_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproduct',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='checkout_products', to='products.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkoutbasket',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_baskets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='checkoutbasket',
            name='billing_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_baskets', to='checkout.billingdetails'),
        ),
        migrations.AlterField(
            model_name='checkoutbasket',
            name='product_basket',
            field=models.ManyToManyField(related_name='checkout_baskets', to='basket.productbasket'),
        ),
        migrations.AlterField(
            model_name='checkoutproduct',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='checkoutproduct',
            name='billing_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_products', to='checkout.billingdetails'),
        ),
    ]
