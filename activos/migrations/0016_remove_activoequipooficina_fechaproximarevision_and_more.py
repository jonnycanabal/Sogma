# Generated by Django 4.1.1 on 2022-11-15 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0015_alter_activoextintor_fotoextintor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activoequipooficina',
            name='fechaProximaRevision',
        ),
        migrations.RemoveField(
            model_name='activoextintor',
            name='fechaProximaRecarga',
        ),
        migrations.RemoveField(
            model_name='activoextintor',
            name='fechaUltimaRecarga',
        ),
        migrations.RemoveField(
            model_name='activovehiculo',
            name='fechaProximoMantenimiento',
        ),
    ]