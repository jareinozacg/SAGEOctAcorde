# -*- coding: utf-8 -*-

from django.test import Client
from django.test import TestCase
import unittest
import datetime
from estacionamientos.controller import *
from estacionamientos.forms import *
from estacionamientos.forms import *
from estacionamientos.models import Estacionamiento


###################################################################
#                    ESTACIONAMIENTO VISTA DISPONIBLE
###################################################################
class SimpleTest(unittest.TestCase):
	# normal
	def setUp(self):
		self.client = Client()

	# normal
	def test_primera(self):
		response = self.client.get('/estacionamientos/')
		self.assertEqual(response.status_code, 200)



###################################################################
#                    ESTACIONAMIENTO_ALL FORM
###################################################################

class SimpleFormTestCase(TestCase):

	# malicia
	def test_CamposVacios(self):
		form_data = {}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_SoloUnCampoNecesario(self):
		form_data = {
			'propietario': 'Pedro'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_DosCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_TresCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_TodosLosCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_PropietarioInvalidoDigitos(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_PropietarioInvalidoSimbolos(self):
		form_data = {
			'propietario': 'Pedro!',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_RIFtamanoinvalido(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V1234567'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_RIFformatoinvalido(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'Kaa123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_AgregarTLFs(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_FormatoInvalidoTLF(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02119322878'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_TamanoInvalidoTLF(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '0219322878'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_AgregarCorreos(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878',
			'email_1': 'adminsitrador@admin.com',
			'email_2': 'usua_rio@users.com'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_CorreoInvalido(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878',
			'email_1': 'adminsitrador@a@dmin.com'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

###################################################################
# ESTACIONAMIENTO_EXTENDED_FORM
###################################################################

	# malicia
	def test_EstacionamientoExtendedForm_UnCampo(self):
		form_data = { 'puestos': 2}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_DosCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_TresCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_CuatroCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_EstacionamientoExtendedForm_CincoCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_EstacionamientoExtendedForm_TodosCamposBien(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# caso borde
	def test_EstacionamientoExtendedForm_Puestos0(self):
		form_data = { 'puestos': 0,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# caso borde
	def test_EstacionamientoExtendedForm_HoraInicioIgualHoraCierre(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(6, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# caso borde
	def test_EstacionamientoExtendedForm_HoraIniReserIgualHoraFinReser(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(7, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_EstacionamientoExtendedForm_StringEnPuesto(self):
		form_data = { 'puestos': 'hola',
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_StringHoraInicio(self):
		form_data = { 'puestos': 2,
								'horarioin': 'holaa',
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NumeroNegativoHoraInicio(self):
		form_data = { 'puestos': 2,
								'horarioin':-1,
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NoneEntarifa(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': None}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NoneEnHorarioReserva(self):
		form_data = { 'puestos': 2,
								'horarioin': 'holaa',
								'horarioout': datetime.time(19, 0),
								'horario_reserin': None,
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_listaEnHoraReserva(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': [datetime.time(14, 0)],
								'tarifa': 12}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

######################################################################
# ESTACIONAMIENTO_EXTENDED pruebas controlador
###################################################################

	# normal
	def test_HorariosValidos(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# malicia
	def test_HorariosInvalido_HoraCierre_Menor_HoraApertura(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 11, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierre_Igual_HoraApertura(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierreReserva_Menor_HoraAperturaReserva(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 11, minute = 0, second = 0)
		x = validarHorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierreReserva_Igual_HoraAperturaReserva(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 12, minute = 0, second = 0)
		x = validarHorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

	# caso borde
	def test_Limite_HorarioValido_Apertura_Cierre(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 12, minute = 0, second = 1)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 12, minute = 0, second = 1)
		x = validarHorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_Limite_Superior_HorarioValido_Apertura_Cierre(self):
		HoraInicio = datetime.time(hour = 0, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 23, minute = 59, second = 59)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 23, minute = 59, second = 59)
		x = validarHorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_InicioReserva_Mayor_HoraCierreEstacionamiento(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 19, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = validarHorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

	# caso borde
	def test_InicioReserva_Mayor_HoraCierreEstacionamiento2(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 19, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = validarHorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

	# malicia
	def test_CierreReserva_Mayor_HoraCierreEstacionamiento(self):
		horaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		horaFin = datetime.time(hour = 18, minute = 0, second = 0)
		reservaInicio = datetime.time(hour = 17, minute = 0, second = 0)
		reservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = validarHorarioEstacionamiento(horaInicio, horaFin, reservaInicio, reservaFin)
		self.assertEqual(x, (False, 'El horario de cierre del estacionamiento debe ser mayor o igual al horario de finalización de las reservas'))

	# malicia
	def test_CierreReserva_Menos_HoraInicioEstacionamiento(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 10, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 11, minute = 0, second = 0)
		x = validarHorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser mayor o igual al horario de apertura del estacionamiento'))



###################################################################
# ESTACIONAMIENTO_RESERVA_FORM
###################################################################

	# malicia
	def test_EstacionamientoReserva_Vacio(self):
		form_data = {}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_EstacionamientoReserva_UnCampo(self):
		form_data = {'inicio':datetime.time(6, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# normal
	def test_EstacionamientoReserva_TodosCamposBien(self):
		form_data = {'inicio':datetime.time(6, 0), 'final':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_EstacionamientoReserva_InicioString(self):
		form_data = {'inicio':'hola',
								'final':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_FinString(self):
		form_data = {'inicio':datetime.time(6, 0),
								'final':'hola'}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_InicioNone(self):
		form_data = {'inicio':None,
								'final':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_finalNone(self):
		form_data = {'inicio':datetime.time(6, 0),
								'final':None}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

###################################################################
# PRUEBAS DE FUNCIONES DEL CONTROLADOR
###################################################################

##############################################################
# Estacionamiento Reserva Controlador
###################################################################

# HorarioReserva, pruebas Unitarias

	# normal
	def test_HorarioReservaValido(self):
		ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 15, minute = 0, second = 0)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_HorarioReservaInvalido_InicioReservacion_Mayor_FinalReservacion(self):
		ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 12, minute = 59, second = 59)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorarioReservaInvalido_TiempoTotalMenor1h(self):
		ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 13, minute = 59, second = 59)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El tiempo de reserva debe ser al menos de 1 hora'))

	# caso borde
	def test_HorarioReservaInvalido_ReservaFinal_Mayor_HorarioCierre(self):
		ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 1)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El horario de cierre de reserva debe estar en un horario válido'))

	# caso borde
	def test_HorarioReservaInvalido_ReservaInicial_Menor_HorarioApertura(self):
		ReservaInicio = datetime.time(hour = 11, minute = 59, second = 59)
		ReservaFin = datetime.time(hour = 15, minute = 0, second = 1)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe estar en un horario válido'))


#===============================================================================
# PRUEBAS UNITARIAS DE FUNCION puedeReservarALas
#===============================================================================

#===============================================================================
# ESTACIONAMIENTO CON 1 PUESTO
#===============================================================================
		
	def testEstacionamientoVacioReservaMinima(self):
		'Esquina: Reserva de 1 min en estacionamiento vacio'
		capacidad = 1
		horaIni = timeDesdeCadena("15:00")
		horaFin = timeDesdeCadena("15:01")
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, []))
		
	def testEstacionamientoVacio(self):
		'Esquina: Reserva de 30 min en estacionamiento vacio'
		capacidad = 1
		horaIni = timeDesdeCadena("15:00")
		horaFin = timeDesdeCadena("15:30")
		puestosOcupados = []
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, puestosOcupados))

	def testReservar30MinEn30MinReservados(self): 
		'Esquina: Reserva en una hora previamente ocupada'
		capacidad = 1
		horaIni = timeDesdeCadena("15:00")
		horaFin = timeDesdeCadena("15:30")
		puestosOcupados = [("15:00", "15:30")]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testReservar30MinEnHoraMayorALaReservada(self): 
		'Frontera: Reserva media hora en otra previamente ocupada'
		capacidad = 1
		capacidad = 1
		horaIni = timeDesdeCadena("15:30")
		horaFin = timeDesdeCadena("16:00")
		puestosOcupados = [("15:00", "15:30")]
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testReservar30MinEnHoraColisionaConReservada1MinIzqui(self):
		'''Frontera: Reserva media hora que colisiona por la izquierda en \
		1 min con una reserva previamente realizada'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:29")
		horaFin = timeDesdeCadena("15:59")
		puestosOcupados = [("15:00", "15:30")]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	def testReservar30MinEnHoraMenorALaReservada(self): 
		'Esquina: Reserva 30 min en otra posteriormente ocupada'
		capacidad = 1
		horaIni = timeDesdeCadena("14:30")
		horaFin = timeDesdeCadena("15:00")
		puestosOcupados = [("15:00", "15:30")]
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testReservar30MinEnHoraColisionaConReservada1MinDere(self):
		'''Frontera: Reserva media hora que colisiona por la derecha en \
		1 min con una reserva previamente realizada'''
		capacidad = 1
		horaIni = timeDesdeCadena("14:31")
		horaFin = timeDesdeCadena("15:01")
		puestosOcupados = [("15:00", "15:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	
	def testReservar31MinSolapandoReserva30MinIzq(self):
		'''Frontera: Reserva 31 min que solapa una reserva de 30 min y 
		sobresale por la izquierda'''
		capacidad = 1
		horaIni = timeDesdeCadena("14:59")
		horaFin = timeDesdeCadena("15:30")
		puestosOcupados = [("15:00", "15:30")]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	
	def testReservar31MinSolapandoReserva30MinDere(self):
		'''Frontera: Reserva 31 min que solapa una reserva de 30 min y 
		sobresale por la derecha'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:00")
		horaFin = timeDesdeCadena("15:31")
		puestosOcupados = [("15:00", "15:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	
	def testReservar32MinSolapandoReserva30MinAmbos(self):
		'''Frontera: Reserva 32 min que solapa una reserva de 30 min y 
		sobresale por ambos lados por 1 min'''
		capacidad = 1
		horaIni = timeDesdeCadena("14:49")
		horaFin = timeDesdeCadena("15:31")
		puestosOcupados = [("15:00", "15:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
		
	def testReserva28MinEntreDosReservasDe30NoBorde(self): 
		'''Normal: Reserva 28 min entre dos reservas de 30 min , sin tocar sus bordes por 1 min'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:31")
		horaFin = timeDesdeCadena("15:59")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
		
	def testReserva29MinEntreDosReservasDe30BordeIzqui(self): 
		'''Frontera: Reserva 29 min entre dos reservas de 30 min , toca borde izquierdo'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:30")
		horaFin = timeDesdeCadena("15:59")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva29MinEntreDosReservasDe30BordeDere(self): 
		'''Frontera: Reserva 29 min entre dos reservas de 30 min , toca borde derecho'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:31")
		horaFin = timeDesdeCadena("16:00")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva30MinEntreDosReservasDe30Bordes(self): 
		'''Frontera: Reserva 30 min entre dos reservas de 30 min , toca ambos bordes'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:30")
		horaFin = timeDesdeCadena("16:00")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva30MinEntreDosReservasDe30InterIzqui(self): 
		'''Frontera: Reserva 30 min entre dos reservas de 30 min , 
		   intersecta por 1 min a la reserva del lado izquierdo
		'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:29")
		horaFin = timeDesdeCadena("15:59")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva30MinEntreDosReservasDe30InterDere(self): 
		'''Frontera: Reserva 30 min entre dos reservas de 30 min , 
		   intersecta por 1 min a la reserva del lado derecho
		'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:31")
		horaFin = timeDesdeCadena("16:01")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva30MinEntreDosReservasDe30SuperponeIzquie(self): 
		'''Frontera: Reserva 30 min superponiendo la reserva del lado izquierdo
		'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:00")
		horaFin = timeDesdeCadena("15:30")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva30MinEntreDosReservasDe30SuperponeDere(self): 
		'''Frontera: Reserva 30 min superponiendo la reserva del lado derecho
		'''
		capacidad = 1
		horaIni = timeDesdeCadena("16:00")
		horaFin = timeDesdeCadena("16:30")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva1HoraEntreDosReservasDe30SolapaIzqui(self): 
		'''Esquina: Reserva 1 hora superponiendo la reserva del lado izquierdo'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:00")
		horaFin = timeDesdeCadena("16:00")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva1HoraEntreDosReservasDe30SolapaDere(self): 
		'''Esquina: Reserva 1 hora superponiendo la reserva del lado derecho'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:30")
		horaFin = timeDesdeCadena("16:30")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva1Hora30MinEntreDosReservasDe30SolapaAmbos(self): 
		'''Esquina: Reserva 1 y media hora superponiendo ambas reservas'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:00")
		horaFin = timeDesdeCadena("16:30")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva32MinEntreDosReservasDe30SolapaAmbosPor1Min(self): 
		'''Esquina: Reserva 32 min solapando por 1 min ambas reservaciones'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:29")
		horaFin = timeDesdeCadena("16:01")
		puestosOcupados = [("15:00", "15:30"), ("16:00", "16:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva28MinEntreReservaDe30MinNoBorde(self): 
		'''Frontera: Reserva 28 min dentro de una reserva ya creada'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:01")
		horaFin = timeDesdeCadena("15:29")
		puestosOcupados = [("15:00", "15:30")]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva29MinEntreReservaDe30MinbordeIzqui(self): 
		'''Frontera: Reserva 29 min dentro de una reserva chocando por la izquierda con el borde élla'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:00")
		horaFin = timeDesdeCadena("15:29")
		puestosOcupados = [("15:00", "15:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))

	def testReserva29MinEntreReservaDe30MinbordeDere(self): 
		'''Frontera: Reserva 29 min dentro de una reserva chocando por la derecha con el borde élla'''
		capacidad = 1
		horaIni = timeDesdeCadena("15:01")
		horaFin = timeDesdeCadena("15:30")
		puestosOcupados = [("15:00", "15:30")] 
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	
	
	##########################
	######### RESERVA 2 puestos
	#############	
	def testReservaEstacionamientoVacio(self):
		'''Normal'''
		capacidad = 2
		horaIni = timeDesdeCadena("8:00")
		horaFin = timeDesdeCadena("9:00")
		puestosOcupados = []
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, puestosOcupados))
		
	def testReservaVariosPuestoLibre(self):
		'''Normal'''
		capacidad = 2
		horaIni = timeDesdeCadena("8:00")
		horaFin = timeDesdeCadena("9:00")
		puestosOcupados = [ ("8:00","9:00") ]
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testReservaMaximaOcupacionLleno(self):
		'''Normal'''
		capacidad = 2
		horaIni = timeDesdeCadena("8:00")
		horaFin = timeDesdeCadena("9:00")
		puestosOcupados = [ ("8:00","9:00"), \
							("8:00","10:00")  ]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testReservaMaximaOcupacionIntersectado(self):
		'''Frontera'''
		capacidad = 2
		horaIni = timeDesdeCadena("7:00")
		horaFin = timeDesdeCadena("8:01")
		puestosOcupados = [ ("8:00","9:00"), \
							("7:00","10:00")  ]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	def testReservaMaximaOcupacionIntersectado2(self):
		'''Frontera'''
		capacidad = 2
		horaIni = timeDesdeCadena("8:59")
		horaFin = timeDesdeCadena("10:00")
		puestosOcupados = [ ("8:00","9:00"), \
							("7:00","10:00")  ]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	def testReservaMaximaOcupacionContenido(self):
		'''Esquina'''
		capacidad = 2
		horaIni = timeDesdeCadena("8:01")
		horaFin = timeDesdeCadena("8:59")
		puestosOcupados = [ ("8:00","9:00"), \
							("7:00","10:00")  ]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	def testReservaMaximaOcupacionAfuera(self):
		'''Esquina'''
		capacidad = 2
		horaIni = timeDesdeCadena("7:59")
		horaFin = timeDesdeCadena("9:01")
		puestosOcupados = [ ("8:00","9:00"), \
							("7:00","10:00")  ]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testReservaConCupo1Hora(self):
		'''Frontera: Reserva 1 hora posible'''
		capacidad = 2
		horaIni = timeDesdeCadena("08:00")
		horaFin = timeDesdeCadena("09:00")
		puestosOcupados = [("7:00","08:00"),              ("09:00","12:00"),\
										   ("8:00","09:00")                 ]
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testReservaConCupo1Minuto(self):
		'''Caso Esquina: Minimo de reserva 1 minuto'''
		capacidad = 2
		horaIni = timeDesdeCadena("08:02")
		horaFin = timeDesdeCadena("08:03")
		puestosOcupados = [("07:00","08:02"),("08:03","10:00"), \
						   ("07:00"         ,         "10:00")  ]
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	def testReserva1MinutoInicioDia(self):
		'''Caso Malicia'''
		capacidad = 2
		horaIni = timeDesdeCadena("00:00")
		horaFin = timeDesdeCadena("00:01")
		puestosOcupados = [ ("00:01","23:59"),\
							("00:00","23:59") ]      		
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testReserva1MinutoInicioDiaRechazado(self):
		'''Caso Malicia'''
		capacidad = 2
		horaIni = timeDesdeCadena("00:00")
		horaFin = timeDesdeCadena("00:01")
		puestosOcupados =  [("00:00","23:59")]*capacidad
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))	
		
	def testReserva1MinutoFinalDia(self):
		'''Caso Malicia'''
		capacidad = 2
		horaIni = timeDesdeCadena("23:58")
		horaFin = timeDesdeCadena("23:59")
		puestosOcupados = [ ("00:00","23:58"),\
							("00:00","23:59") ]      		
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	def testReserva1MinutoFinalDiaRechazado(self):
		'''Caso Malicia'''
		capacidad = 2
		horaIni = timeDesdeCadena("23:58")
		horaFin = timeDesdeCadena("23:59")
		puestosOcupados = [ ("00:00","23:59")]*capacidad     		
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testReservaSolapamientoExtremoIzquierdo(self):
		'''Caso Frontera: Solapamiento izquierdo intervalo max ocupacion'''
		capacidad = 2
		horaIni = timeDesdeCadena("07:59")
		horaFin = timeDesdeCadena("09:00")
		puestosOcupados =  [("07:00","08:00"),("09:00","10:00"),\
							("07:00"         ,         "10:00") ]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testReservaSolapamientoExtremoDerecho(self):
		'''Caso frontera: Solapamiento derecho invervalo max ocupacion'''
		capacidad = 2
		horaIni = timeDesdeCadena("08:00")
		horaFin = timeDesdeCadena("09:01")
		puestosOcupados =  [("07:00","08:00"),("09:00","10:00"),\
							("07:00"           ,       "10:00")]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	def testReservaSolapamientoDosExtremos(self):
		'''Caso Esquina: Solapamiento derecho e izquierdo invervalo max.'''
		capacidad = 2
		horaIni = timeDesdeCadena("07:59")
		horaFin = timeDesdeCadena("09:01")
		puestosOcupados =  [("07:00","08:00"),("09:00","10:00"),\
							("07:00","08:00"),("09:00","10:00") ]                   
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
	
	def testPuestosOcupadosSinSolapamiento(self):
		''' 
		Prueba Frontera ( Caso interesante). 
		Es necesario un movimiento de reservas(o puestos) del puesto 2 al puesto 1
		'''
		capacidad = 2
		horaIni = timeDesdeCadena("07:00")
		horaFin = timeDesdeCadena("09:00")
		puestosOcupados =  [("07:00","08:00"),               \
							                ("08:00","09:00")]
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	def testPuestosOcupadosUnSolapamiento(self):
		'''
		Prueba Esquina ( Caso interesante)
		No es posible un movimiento de reservas(o puestos)
		'''
		capacidad = 2
		horaIni = timeDesdeCadena("07:00")
		horaFin = timeDesdeCadena("09:00")
		puestosOcupados =  [("07:00","08:00"),               \
							                ("07:59","09:00")]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	def testPuestosOcupadosUnSolapamiento2(self):
		'''Prueba Malicia ( Caso interesante) '''
		capacidad = 2
		horaIni = timeDesdeCadena("07:00")
		horaFin = timeDesdeCadena("10:00")
		puestosOcupados =  [("07:00","08:00")       ,       ("09:00","10:00"),\
							                ("8:00","09:01")                 ]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))
		
	def testPuestosOcupadosVariosSolapamientos(self):
		'''Prueba Malicia ( Caso interesante) '''
		capacidad = 2
		horaIni = timeDesdeCadena("07:00")
		horaFin = timeDesdeCadena("10:00")
		puestosOcupados =  [("07:00","08:00")       ,       ("09:00","10:00"),\
							                ("7:59","09:01")                 ]
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, crearTuplasHorasDesdeListaCadena(puestosOcupados)))   
#===============================================================================
#
# 	
# 	def testReservaDosHorasEnReservaMaxima(self): # Esquina (Manuel) Linea 65
# 		capacidad = 10
# 		reservas  = [(8,10),(15,17)]*capacidad
# 		reserva = (15,16)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		self.assertEqual(estacionamiento.reservar(*reserva),False)
#
# 	
# 	
# 	def testReserva1HoraEntrePrimeraSobreposicionReservas(self): #esquina maliciosa  (Manuel) Linea 133
# 		capacidad = 10
# 		reservas  = [(6,7),(7,8)]*capacidad
# 		reserva = (6,7)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		self.assertEqual(estacionamiento.reservar(*reserva),False)
# 	
# 	
# 	def testReservaCeroHoras(self): #Esquina  (Manuel) Linea 152
# 		pass
# 	
# 	def testReservaAntesdelas6(self): # Malicia frontera (Manuel) Linea 156
# 		pass
# 	
# 	def testReservaLuegodelas18(self): #Malicia (Manuel) Linea 161
# 		pass
# 	
# 	def testReservaHoraFinalMenorHoraInicialValidas(self): #Malicia (Manuel) Linea 166
# 		pass
# 	
# 	def testReservaAntesdeLas6Inclusive(self): #Malicia Frontera (Manuel) Linea 171
# 		pass
# 	
# 	def testReservaLuegodelas18Inclusive(self): #Malicia frontera (Manuel) Linea 176
# 		pass
# 				
# 	def testReservacionInvalida_EntradaMenor(self): # Frontera (Daniel) Linea 52
# 		pass
# 	
# 	def testReservacionInvalida_HoraEntradaMayor(self): #Frontera (Daniel) Buena la idea pero mal horario
# 		pass
# 
#
# 	
# 	def testJesus1(self): # Conjunto de reservaciones sin objetivo unico (Jesus) Linea 10
# 		capacidad = 10
# 		reservas = []
# # 		a_reservar = ((8,12), (11,13), (10,12), (9,12), (7,12), (10,12), (7,12),(9,15), (10,18), (11, 14))
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		
# 		for reserva in a_reservar:
# 			assert estacionamiento.reservar(*reserva)
# 	
# 	def testFullParking(self):#Casos por malicia (Jesus) Linea 29
# 		capacidad = 10
# 		a_reservar = ((8,12), (11,13), (10,12), (9,12), (7,12), (10,12), (7,12),(9,15), (10,18), (11, 14))
# 		estacionamiento = Estacionamiento(capacidad,[])		
# 		
# 		for reserva in a_reservar:
# 			assert estacionamiento.reservar(*reserva)
# 		
# 		self.assertEqual(estacionamiento.reservar(9,13),False)
# 		
# 	def testReservaMaximaContenidaReservaUsuario(self): # Esquina agregada por Manuel
# 		estacionamiento = Estacionamiento(1,[(11,12)])		
# 		self.assertEqual(estacionamiento.reservar(10,13),False)
# 
# 	def testReservaMaximaContenidaReservaUsuarioDisponible(self): # Esquina agregada por Manuel
# 		estacionamiento = Estacionamiento(2,[(11,12)])
# 		self.assertEqual(estacionamiento.reservar(10,13),True)
# 
# 	def testReservaMaximaContenidaReservaUsuarioNoDisponibleDos(self): # Esquina agregada por Manuel
# 		estacionamiento = Estacionamiento(2,[(11,12)]*2)
# 		self.assertEqual(estacionamiento.reservar(10,13),False)
# 		
# 	def testCarrosMismoHorario(self):# Conjunto de reservaciones sin objetivo unico (Daniel) Linea 60
# 		capacidad = 10
# 		a_reservar = ((10, 12),(8, 12),(10, 12),(10, 12),(10, 12),(7, 12),(6, 12),(9, 12),(10, 12),(10, 12))
# 		estacionamiento = Estacionamiento(capacidad,[])		
# 		
# 		for reserva in a_reservar:
# 			assert estacionamiento.reservar(*reserva)
# 		
# 	def testOnceCarrosMismoHorario(self): # Conjunto de reservaciones sin objetivo unico (Daniel) Linea 63
# 		capacidad = 10
# 		a_reservar = ((10, 12),(8, 12),(10, 12),(10, 12),(10, 12),(7, 12),(6, 12),(9, 12),(10, 12),(10, 12))
# 		estacionamiento = Estacionamiento(capacidad,[])		
# 		
# 		for reserva in a_reservar:
# 			assert estacionamiento.reservar(*reserva)
# 		
# 		self.assertEqual(estacionamiento.reservar(7,12),False)
# 		
# 	def testExtremadamenteGrandeUnaHoraFinalNoDisponible(self): # Esquina agregada por Manuel
# 		capacidad =4200
# 		estacionamiento = Estacionamiento(capacidad,[(6,18)]*capacidad)		
# 		self.assertEqual(estacionamiento.reservar(17,18),False)
# 	
# 	def testExtremadamenteGrandeUnaHoraInicioNoDisponible(self): # Esquina agregada por Manuel
# 		capacidad =4200
# 		estacionamiento = Estacionamiento(capacidad,[(6,18)]*capacidad)		
# 		
# 		self.assertEqual(estacionamiento.reservar(6,7),False)
# 
# 	def testExtremadamenteGrandeUnaHoraDisponible(self): # Esquina agregada por Manuel
# 		capacidad = 1000
# 		estacionamiento = Estacionamiento(capacidad,[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18)]*(capacidad - 1) +\
# 						 [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16)])
# 		self.assertEqual(estacionamiento.reservar(17,18),True)
#===============================================================================
