# Generated by Django 4.1.1 on 2022-11-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionActivos', '0018_alter_registrarmantenimiento_descripcionmantenimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generarruta',
            name='descripcionRuta',
            field=models.TextField(max_length=500, verbose_name='Descripción'),
        ),
    ]
