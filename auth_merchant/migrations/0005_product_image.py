# Generated by Django 5.0 on 2024-01-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_merchant', '0004_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product_images/'),
        ),
    ]
