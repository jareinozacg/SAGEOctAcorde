# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Propietario', models.CharField(max_length=50, help_text='Nombre Propio')),
                ('Nombre', models.CharField(max_length=50)),
                ('Direccion', models.TextField(max_length=120)),
                ('Telefono_1', models.CharField(null=True, max_length=30, blank=True)),
                ('Telefono_2', models.CharField(null=True, max_length=30, blank=True)),
                ('Telefono_3', models.CharField(null=True, max_length=30, blank=True)),
                ('Email_1', models.EmailField(null=True, max_length=75, blank=True)),
                ('Email_2', models.EmailField(null=True, max_length=75, blank=True)),
                ('Rif', models.CharField(max_length=12)),
                ('Apertura', models.TimeField(null=True, blank=True)),
                ('Cierre', models.TimeField(null=True, blank=True)),
                ('Reservas_Inicio', models.TimeField(null=True, blank=True)),
                ('Reservas_Cierre', models.TimeField(null=True, blank=True)),
                ('NroPuesto', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReservasModel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Puesto', models.IntegerField()),
                ('InicioReserva', models.TimeField()),
                ('FinalReserva', models.TimeField()),
                ('Estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=2)),
                ('granularidad', models.CharField(default='hrs', max_length=4, choices=[('min', 'Minutos'), ('hrs', 'Horas')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='Tarifa',
            field=models.ForeignKey(null=True, to='estacionamientos.Tarifa', blank=True),
            preserve_default=True,
        ),
    ]
