# Generated by Django 5.2.1 on 2025-06-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0003_alter_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.CharField(default='Sin categoria', max_length=80),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]
