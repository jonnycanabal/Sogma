# Generated by Django 4.1.1 on 2022-11-20 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0018_alter_activoequipooficina_memoriaequipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activoextintor',
            name='pesoExtintor',
            field=models.CharField(max_length=3, verbose_name='Peso del Extintor'),
        ),
    ]
