# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import *

admin.site.register(Estacionamiento)
admin.site.register(ReservasModel)

# Register your models here.
@admin.register(Tarifa)
class adminTarifa(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)