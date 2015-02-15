# -*- coding: utf-8 -*-

from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm
from _overlapped import NULL
import datetime


class Estacionamiento(models.Model):
	min_hora = datetime.time(0, 0)
	max_hora = datetime.time(23, 59)
	# propietario=models.ForeignKey(Propietario)
	Propietario = models.CharField(max_length = 50, help_text = "Nombre Propio")
	Nombre = models.CharField(max_length = 50)
	Direccion = models.TextField(max_length = 120)

	Telefono_1 = models.CharField(blank = True, null = True, max_length = 30)
	Telefono_2 = models.CharField(blank = True, null = True, max_length = 30)
	Telefono_3 = models.CharField(blank = True, null = True, max_length = 30)

	Email_1 = models.EmailField(blank = True, null = True)
	Email_2 = models.EmailField(blank = True, null = True)

	Rif = models.CharField(max_length = 12)

	Apertura = models.TimeField(blank = True, null = True, default=min_hora)
	Cierre = models.TimeField(blank = True, null = True, default=max_hora)
	Reservas_Inicio = models.TimeField(blank = True, null = True, default=min_hora)
	Reservas_Cierre = models.TimeField(blank = True, null = True, default=max_hora)
	NroPuesto = models.IntegerField(blank = True, null = True, default = 10)
	Tarifa = models.ForeignKey('Tarifa', null = True, blank = True, default = 10.00)


class ReservasModel(models.Model):
	Estacionamiento = models.ForeignKey(Estacionamiento)
	InicioReserva = models.TimeField()
	FinalReserva = models.TimeField()

class Tarifa(models.Model):
	tipo_granularidad = (("min","Minutos"), ("hrs","Horas"),)
	
	nombre = models.CharField(max_length= 25)
	tarifa = models.DecimalField( max_digits = 10, decimal_places=2, blank = True )
	granularidad = models.CharField(default = "hrs", max_length = 4, choices = tipo_granularidad, blank = False)
	
	def __str__(self):              # __unicode__ on Python 2
		return str(self.nombre)
