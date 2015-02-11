# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0003_auto_20150211_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='Tarifa',
            field=models.ForeignKey(null=True, default=None, to='estacionamientos.Tarifa'),
            preserve_default=True,
        ),
    ]
