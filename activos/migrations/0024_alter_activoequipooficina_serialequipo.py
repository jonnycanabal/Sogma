# Generated by Django 4.1.1 on 2022-11-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0023_alter_activoextintor_serialextintor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activoequipooficina',
            name='serialEquipo',
            field=models.CharField(max_length=50, unique=True, verbose_name='Serial Equipo'),
        ),
    ]
