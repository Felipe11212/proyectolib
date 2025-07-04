# Generated by Django 5.2.3 on 2025-06-27 00:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inventario', models.DateField()),
                ('producto', models.CharField(default='Sin categoría', max_length=80)),
                ('stock', models.CharField(default='Sin categoría', max_length=80)),
                ('comentario', models.CharField(default='Sin categoría', max_length=80)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='inventarios/')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_stock', models.IntegerField()),
                ('nombre_producto', models.CharField(default='Sin categoría', max_length=100)),
                ('categoria', models.CharField(default='Sin categoría', max_length=50)),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='inventariolib.inventario')),
            ],
        ),
    ]
