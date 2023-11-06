# Generated by Django 4.2.6 on 2023-11-06 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_is_published_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
            preserve_default=False,
        ),
    ]