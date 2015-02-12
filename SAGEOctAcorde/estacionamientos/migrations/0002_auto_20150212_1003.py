# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=2)),
                ('granularidad', models.CharField(choices=[('min', 'Minutos'), ('hrs', 'Horas')], max_length=4, default='hrs')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='Tarifa',
            field=models.ForeignKey(blank=True, to='estacionamientos.Tarifa', null=True),
            preserve_default=True,
        ),
    ]
