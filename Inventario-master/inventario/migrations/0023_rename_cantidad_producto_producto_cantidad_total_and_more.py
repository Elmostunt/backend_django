# Generated by Django 4.2.3 on 2023-12-14 02:38

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0022_alter_perfilusuario_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='cantidad_producto',
            new_name='cantidad_total',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='bodegas',
        ),
        migrations.AlterField(
            model_name='perfilusuario',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Usuario'),
        ),
        migrations.CreateModel(
            name='ProductoBodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(default=0)),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_bodega', to='inventario.bodega')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bodega_producto', to='inventario.producto')),
            ],
            options={
                'unique_together': {('bodega', 'producto')},
            },
        ),
    ]
