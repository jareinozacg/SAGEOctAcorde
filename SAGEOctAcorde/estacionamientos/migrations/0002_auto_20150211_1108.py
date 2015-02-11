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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('tarifa', models.DecimalField(max_digits=10, decimal_places=2)),
                ('granularidad', models.CharField(default='hrs', choices=[('min', 'Minutos'), ('hrs', 'Horas')], max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='Tarifa',
            field=models.ForeignKey(to='estacionamientos.Tarifa'),
            preserve_default=True,
        ),
    ]
