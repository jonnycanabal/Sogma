# Generated by Django 4.1.1 on 2022-10-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0004_activoequipooficina_estado_activovehiculo_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activoequipooficina',
            old_name='estado',
            new_name='estadoEquipo',
        ),
        migrations.RenameField(
            model_name='activoextintor',
            old_name='estado',
            new_name='estadoExtintor',
        ),
        migrations.RemoveField(
            model_name='activovehiculo',
            name='estado',
        ),
        migrations.AddField(
            model_name='activovehiculo',
            name='condicionVehiculo',
            field=models.CharField(choices=[('Nuevo', 'Nuevo'), ('Usado', 'Usado')], default='Nuevo', max_length=10, verbose_name='Estado del Vehículo'),
        ),
        migrations.AlterField(
            model_name='activovehiculo',
            name='estadoVehiculo',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Estado'),
        ),
    ]
