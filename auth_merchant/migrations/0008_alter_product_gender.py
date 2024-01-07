# Generated by Django 5.0 on 2024-01-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_merchant', '0007_product_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]