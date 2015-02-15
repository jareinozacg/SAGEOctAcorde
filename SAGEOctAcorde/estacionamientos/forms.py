# -*- coding: utf-8 -*-

from django import forms
from decimal import Decimal
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
                    ]
                )

    nombre = forms.CharField(required = True, label = "Nombre")

    direccion = forms.CharField(required = True)

    telefono_1 = forms.CharField(required = False, validators = [phone_validator])
    telefono_2 = forms.CharField(required = False, validators = [phone_validator])
    telefono_3 = forms.CharField(required = False, validators = [phone_validator])

    email_1 = forms.EmailField(required = False)
    email_2 = forms.EmailField(required = False)

    rif = forms.CharField(
                    required = True,
                    label = "RIF",
                    validators = [
                          RegexValidator(
                                regex = '^[JVD]-?\d{8}-?\d$',
                                message = 'Introduzca un RIF con un formato válido.'
                        )
                    ]
                )

class EstacionamientoExtendedForm(ModelForm):
    
    Tarifa = forms.ModelChoiceField(
        queryset=Tarifa.objects.all(), 
        empty_label="Seleccione tipo de Tarifa",
        required = False
        )

    monto = forms.DecimalField( max_digits = 10, decimal_places=2, label = 'Monto', 
                                required = False)
    
    class Meta:
        model = Estacionamiento
        exclude = ['Propietario','Nombre','Direccion', 'Telefono_1', 'Telefono_2','Telefono_3',
                    'Email_1','Email_2','Rif', 'Tarifa']
        
    def clean(self):
        if  isinstance(self.cleaned_data['monto'], Decimal):
            if self.cleaned_data['monto'] <= 0.0 :
                raise forms.ValidationError({'monto': ["El valor debe ser positivo.",]})
        if  isinstance(self.cleaned_data['NroPuesto'], Decimal):
            if self.cleaned_data['NroPuesto'] <= 0.0:
                raise forms.ValidationError({'NroPuesto': ["El valor debe ser positivo.",]})
        super(EstacionamientoExtendedForm, self).clean()


class EstacionamientoReserva(forms.Form):
    inicio = forms.TimeField(label = 'Horario de inicio')
    final = forms.TimeField(label = 'Horario final')

class DefinirTarifa(ModelForm):
    class Meta:
        model = Tarifa
        exclude = ['nombre']