# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from estacionamientos.models import *
from django.core.validators import RegexValidator
from django.template.defaultfilters import default


class EstacionamientoForm(forms.Form):

    phone_validator = RegexValidator(
                            regex = '^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
                            message = 'Debe introducir un formato válido.'
                        )

    # nombre del dueno (no se permiten digitos)
    propietario = forms.CharField(
                    required = True,
                    label = "Propietario",
                    validators = [
                          RegexValidator(
                                regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚ ]+$',
                                message = 'Sólo debe contener letras.'
                        )
                    ],
                    help_text="Nombre del propietario del estacionamiento."
                )

    nombre = forms.CharField(required = True, label = "Nombre",
                    help_text="Nombre del estacionamiento.")

    direccion = forms.CharField(required = True,
                    help_text="Dirección del estacionamiento.")

    telefono_1 = forms.CharField(required = False, validators = [phone_validator],
                    help_text="Telefono de contacto. Ejemplo : 0426-1234567")
    telefono_2 = forms.CharField(required = False, validators = [phone_validator],
                    help_text="Telefono de contacto. Ejemplo : 0426-1234567")
    telefono_3 = forms.CharField(required = False, validators = [phone_validator],
                    help_text="Telefono de contacto. Ejemplo : 0426-1234567")

    email_1 = forms.EmailField(required = False,
                    help_text="Correo de contacto. Ejemplo : octacorde@gmail.com")
    email_2 = forms.EmailField(required = False,
                    help_text="Correo de contacto. Ejemplo : octacorde@gmail.com")

    rif = forms.CharField(
                    required = True,
                    label = "RIF",
                    validators = [
                          RegexValidator(
                                regex = '^[JVD]-?\d{8}-?\d$',
                                message = 'Introduzca un RIF con un formato válido.'
                        )
                    ],
                    help_text="Rif del estacionamiento. Ejemplo : J-00000000-0"
                )

class EstacionamientoExtendedForm(ModelForm):
    Tarifa = forms.ModelChoiceField(
        queryset=Tarifa.objects.all(), 
        empty_label="Seleccione tipo de Tarifa",
        required = True
        )

    monto = forms.DecimalField( max_digits = 10, decimal_places=2,
                                 label = 'Monto', required = False)
    
    class Meta:
        model = Estacionamiento
        exclude = ['Propietario','Nombre','Direccion', 'Telefono_1', 'Telefono_2','Telefono_3',
                    'Email_1','Email_2','Rif', 'Tarifa']


class EstacionamientoReserva(forms.Form):
    inicio = forms.TimeField(label = 'Horario de inicio',\
                             help_text="Hora de inicio de la reserva en formato militar. Ejemplo : 13:01")
    final = forms.TimeField(label = 'Horario final',\
                             help_text="Hora final de la reserva en formato militar. Ejemplo : 14:01")

class DefinirTarifa(ModelForm):
    class Meta:
        model = Tarifa
        exclude = ['nombre']