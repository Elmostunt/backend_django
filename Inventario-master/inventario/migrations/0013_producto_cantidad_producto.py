# Generated by Django 4.2.3 on 2023-07-21 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0012_alter_detallemovimiento_cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad_producto',
            field=models.IntegerField(default=0),
        ),
    ]
