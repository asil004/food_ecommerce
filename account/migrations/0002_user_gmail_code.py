# Generated by Django 5.0.3 on 2024-04-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gmail_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
