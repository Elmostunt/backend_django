# Generated by Django 4.2.1 on 2023-11-24 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_categoria_transaccion_producto_detalletransaccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservarhora',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='myapp.project'),
        ),
    ]
