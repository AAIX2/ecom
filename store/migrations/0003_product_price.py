# Generated by Django 5.0.4 on 2024-04-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_user_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=None),
        ),
    ]
