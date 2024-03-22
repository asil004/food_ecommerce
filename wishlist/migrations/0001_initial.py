# Generated by Django 5.0.3 on 2024-03-22 10:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_remove_color_color_remove_color_product_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='products.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]