# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_auto_20150211_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='Tarifa',
            field=models.ForeignKey(to='estacionamientos.Tarifa', default=None),
            preserve_default=True,
        ),
    ]
