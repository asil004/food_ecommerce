# Generated by Django 5.0.3 on 2024-03-28 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_productcheckout_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcheckout',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productcheckout',
            name='size',
        ),
    ]