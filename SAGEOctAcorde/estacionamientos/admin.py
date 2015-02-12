# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import Estacionamiento, ReservasModel, Tarifa

admin.site.register(Estacionamiento)
admin.site.register(ReservasModel)

@admin.register(Tarifa)
class adminCursa(admin.ModelAdmin):
    list_display = ('nombre', 'tarifa')
    search_fields = ('nombre',)
    list_filter = ('tarifa',)