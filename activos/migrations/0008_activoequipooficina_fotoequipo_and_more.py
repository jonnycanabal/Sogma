# Generated by Django 4.1.1 on 2022-11-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0007_alter_activovehiculo_fechafinsoat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activoequipooficina',
            name='fotoEquipo',
            field=models.ImageField(blank=True, default='equipos/equipo_default.jpg', upload_to='equipos'),
        ),
        migrations.AddField(
            model_name='activoextintor',
            name='fotoExtintor',
            field=models.ImageField(blank=True, default='extintores/extintores_default.jpg', upload_to='extintores'),
        ),
        migrations.AddField(
            model_name='activovehiculo',
            name='fotoEquipo',
            field=models.ImageField(blank=True, default='vehiculos/vehiculo_default.jpg', upload_to='vehiculos'),
        ),
    ]
