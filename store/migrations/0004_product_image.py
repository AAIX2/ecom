# Generated by Django 5.0.4 on 2024-05-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]