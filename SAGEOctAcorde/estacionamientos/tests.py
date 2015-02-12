# -*- coding: utf-8 -*-

from django.test import Client
from django.test import TestCase
import unittest
import datetime
from estacionamientos.controller import *
from estacionamientos.forms import *
from estacionamientos.forms import *
from estacionamientos.views import tablaMarzullo


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
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# malicia
	def test_HorariosInvalido_HoraCierre_Menor_HoraApertura(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 11, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierre_Igual_HoraApertura(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierreReserva_Menor_HoraAperturaReserva(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 11, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierreReserva_Igual_HoraAperturaReserva(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 12, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

	# caso borde
	def test_Limite_HorarioValido_Apertura_Cierre(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 12, minute = 0, second = 1)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 12, minute = 0, second = 1)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_Limite_Superior_HorarioValido_Apertura_Cierre(self):
		HoraInicio = datetime.time(hour = 0, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 23, minute = 59, second = 59)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 23, minute = 59, second = 59)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_InicioReserva_Mayor_HoraCierreEstacionamiento(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 19, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

	# caso borde
	def test_InicioReserva_Mayor_HoraCierreEstacionamiento2(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 19, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

	# malicia
	def test_CierreReserva_Mayor_HoraCierreEstacionamiento(self):
		horaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		horaFin = datetime.time(hour = 18, minute = 0, second = 0)
		reservaInicio = datetime.time(hour = 17, minute = 0, second = 0)
		reservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(horaInicio, horaFin, reservaInicio, reservaFin)
		self.assertEqual(x, (False, 'El horario de cierre del estacionamiento debe ser mayor o igual al horario de finalización de las reservas'))

	# malicia
	def test_CierreReserva_Menos_HoraInicioEstacionamiento(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 10, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 11, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
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


	'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	''  CASOS DE PRUEBA DESDE AQUI
	'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#===============================================================================
# 	def testEstacionamientoVacio(self): #Frontera
# 		capacidad = 10
# 		horaIni = datetime.time(6)
# 		horaFin = datetime.time(18)
# 		tablaMarzullo = []
# 		
# 		assert puedeReservarALas(horaIni, horaFin, capacidad, tablaMarzullo)
# 
# 	def testReservarUnaHoraEnHoraReservada(self): #Frontera
# 		
# 		capacidad = 10
# 		horaIni = datetime.time(9)
# 		horaFin = datetime.time(11)
# 		tablaMarzullo = [(datetime.time(9) , -1 , 1),\
# 						 (datetime.time(11) , 1 , 1*capacidad)] * capacidad		
# 		tablaMarzullo.sort(key=functools.cmp_to_key(compararTuplasMarzullo))
# 
# 		
# 		assert len(puedeReservarALas(horaIni, horaFin, capacidad, tablaMarzullo)) == 1
# 	
# 	def testReservarUnaHoraEnHoraMayorALaReservada(self): #Frontera (Manuel) Linea 45
# 		capacidad = 10
# 		horaIni = datetime.time(15)
# 		horaFin = datetime.time(16)
# 		tablaMarzullo = [(datetime.time(9) , -1 , 1),\
# 						 (datetime.time(11) , 1 , 1)]*capacidad
# 		tablaMarzullo.sort(key=functools.cmp_to_key(compararTuplasMarzullo))
# 		
# 		
# 		assert puedeReservarALas(horaIni, horaFin, capacidad, tablaMarzullo)
# 		
# 	def testReservarUnaHoraEnHoraMenorALaReservada(self): #Frontera (Manuel) Linea 55
# 		capacidad = 10
# 		horaIni = datetime.time(7)
# 		horaFin = datetime.time(8)
# 		tablaMarzullo = [(datetime.time(9) , -1 , 1),\
# 						 (datetime.time(11) , 1 , 1)]*capacidad
# 		tablaMarzullo.sort(key=functools.cmp_to_key(compararTuplasMarzullo))
# 		
# 		
# 		assert puedeReservarALas(horaIni, horaFin, capacidad, tablaMarzullo)
#===============================================================================
	
	def formatHora(self,hora):
		'''
		Funcion que dado una fecha en formato string, devuelve el datetime
		'''
		return datetime.datetime.strptime(hora, "%H:%M") # "%Y-%m-%d %H:%M" formato para fechas
	
	def crearTuplasHoras(self,listaTuplas):
		'''
		Convierte tuplas de string a datetime
		'''
		listaHora = []
		
		for tupla in listaTuplas:
			listaHora.append( (self.formatHora(tupla[0]),self.formatHora(tupla[1])) )
		
		return listaHora
				
		
	def testReservarEjemplo(self):
		'''
		Ejemplo Formato
		'''
		capacidad = 10
		horaIni = self.formatHora("16:00")
		horaFin = self.formatHora("17:00")
		puestosOcupados = self.crearTuplasHoras(                              \
					[("16:00", "18:00"), ("3:00", "9:00")]                    \
		)
		tablaMarzullo = crearTablaMarzullo(puestosOcupados)
		# Opcion 1
		self.assertTrue(puedeReservarALas(horaIni, horaFin, capacidad, tablaMarzullo))
		# Opcion 2
	#	self.assertRaises(AssertionError, puedeReservarALas, horaIni,horaFin,capacidad,tablaMarzullo)
		
	def testReservaDosHorasEnReservaMaxima(self): # Esquina (Manuel) Linea 65
		capacidad = 10
		horaIni = self.formatHora("15:00")
		horaFin = self.formatHora("16:00")
		puestosOcupados = self.crearTuplasHoras(                              \
					[("08:00", "10:00"), ("15:00", "17:00")]*capacidad        \
		) 
		tablaMarzullo = crearTablaMarzullo(puestosOcupados)
		self.assertFalse(puedeReservarALas(horaIni, horaFin, capacidad, tablaMarzullo))
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
# 	def testReserva1HoraEntreCompletaReserva(self): # Esquina (Manuel) Linea 74
# 		capacidad = 10
# 		reservas  = [(6,10),(11,18)]*capacidad
# 		reserva = (10,11)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		assert estacionamiento.reservar(*reserva)
# 		
# 	
# 	def testReserva1HoraAlInicioEntreCompletaReserva(self): #Esquina (Manuel) Linea 83 
# 		capacidad = 10
# 		reservas  = [(7,18)]*capacidad
# 		reserva = (6,7)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		assert estacionamiento.reservar(*reserva)
# 	
# 	def testReserva1HoraAlFinalEntreCompletaReserva(self): #Esquina(Manuel) Linea 91
# 		capacidad = 10
# 		reservas  = [(6,17)]*capacidad
# 		reserva = (17,18)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		assert estacionamiento.reservar(*reserva)
# 	
# 	def testReserva1HoraInicioConCompletaReserva(self): # Esquina (Manuel) Linea 99
# 		capacidad = 10
# 		reservas  = [(6,18)]*capacidad
# 		reserva = (6,7)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		self.assertEqual(estacionamiento.reservar(*reserva),False)
# 	
# 	def testReserva1HoraFinalConCompletaReserva(self): #Esquina (Manuel) Linea 107
# 		capacidad = 10
# 		reservas  = [(6,18)]*capacidad
# 		reserva = (17,18)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		self.assertEqual(estacionamiento.reservar(*reserva),False)
# 	
# 	
# 	def testReserva1HoraDespuesSobreposicionReservas(self): #Esquina maliciosa (Manuel)  Linea 115
# 		capacidad = 10
# 		reservas  = [(6,7),(7,8)]*capacidad
# 		reserva = (8,9)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		assert estacionamiento.reservar(*reserva)
# 	
# 	
# 	def testReserva1HoraAntesSobreposicionReservas(self): #Esquina maliciosa (Manuel)  Linea 124
# 		capacidad = 10
# 		reservas  = [(7,8),(8,9)]*capacidad
# 		reserva = (6,7)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		assert estacionamiento.reservar(*reserva)
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
# 	def testReserva1HoraEntreSegundaSobreposicionReservas(self): #Esquina maliciosa (Manuel)  Linea 142
# 		capacidad = 10
# 		reservas  = [(6,7),(7,8)]*capacidad
# 		reserva = (7,8)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		self.assertEqual(estacionamiento.reservar(*reserva),False)
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
# 	def testReservaSinCupoExtremosIguales(self): #Esquina (Chino) Linea 27
# 		capacidad = 1
# 		reservas  = [(8,10)]*capacidad
# 		reserva = (8,10)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		self.assertEqual(estacionamiento.reservar(*reserva),False)
# 	
# 	def testReservaSinCupoExtremosDiferentes(self): # Esquina (Chino) Linea 33
# 		capacidad = 1
# 		reservas  = [(8,12)]*capacidad
# 		reserva = (9,13)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		self.assertEqual(estacionamiento.reservar(*reserva),False)
# 		
# 	def testReservaConCupo(self): #Esquina (Chino) Linea 39
# 		capacidad = 1
# 		reservas  = [(8,12),(14,17)]*capacidad
# 		reserva = (12,14)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		assert estacionamiento.reservar(*reserva)
# 		
# 	def testReservaConCupoDosPuestos(self): # Esquina (Chino) Linea 45 , modificar segundo horario
# 		capacidad = 2
# 		reservas  = [(8,12),(14,17)]*capacidad
# 		reserva = (12,14)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		assert estacionamiento.reservar(*reserva)
# 	
# 	def testReservaSinCupoDosExtremos(self): #Esquina (Chino) Linea 52 (se puede dividir en dos pruebas por cada extremo)
# 		capacidad = 1
# 		reservas  = [(8,12),(14,17)]*capacidad
# 		reserva = (11,15)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		self.assertEqual(estacionamiento.reservar(*reserva),False)
# 	
# 	def testReservaSinCupoDosExtremosDosPuestos(self): #Esquina (Chino) Linea 58 (se puede dividir , arreglar segundo horario)
# 		capacidad = 1
# 		reservas  = [(8,12),(14,17)]*capacidad
# 		reserva = (12,15)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		self.assertEqual(estacionamiento.reservar(*reserva),False)
# 		
# 	def testPuestosLlenos(self): #Esquinas maliciosas  (Chino) Linea 65 (dividir tal vez?) cuestionable...
# 		capacidad = 3
# 		reservas = [(6,17),(17,18), 
# 					(6,8), (8,18), 
# 					(6,12),(12,13),(13,18)]
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)
# 		
# 		self.assertEqual(estacionamiento.reservar(17,18),False)
# 		self.assertEqual(estacionamiento.reservar(6,7),False)
# 		self.assertEqual(estacionamiento.reservar(6,18),False)
# 	
# 	def testPuestoSuperLlenosconAlgunPuestoVacio(self): #Esquina maliciosa (Chino) Linea 83
# 		capacidad = 10
# 		reservas  = [(6,18)]*(capacidad-1) + [(6,17)] 
# 		reserva = (17,18)
# 		
# 		estacionamiento = Estacionamiento(capacidad,reservas)		
# 		assert estacionamiento.reservar(*reserva)
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
