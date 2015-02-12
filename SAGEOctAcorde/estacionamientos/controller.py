# -*- coding: utf-8 -*-

# Archivo con funciones de control para SAGE
import functools


def HorarioEstacionamiento(aperturaEst, finalEst, inicioReservaEst, finalReservaEst):
	'''
		Chequea que el horario de estacionamiento de apertura y el horario de apertura 
		de las reservas esten correctos.
	'''
	if aperturaEst >= finalEst:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if inicioReservaEst >= finalReservaEst:
		return (False, 'El horario de inicio de reserva debe ser menor al horario de cierre')
	if inicioReservaEst < aperturaEst:
		return (False, 'El horario de inicio de reserva debe ser mayor o igual al horario de apertura del estacionamiento')
	if inicioReservaEst > finalEst:
		return (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento')
	if finalReservaEst < aperturaEst:
		return (False, 'El horario de apertura del estacionamiento debe ser menor al horario de finalización de las reservas')
	if finalReservaEst > finalEst:
		return (False, 'El horario de cierre del estacionamiento debe ser mayor o igual al horario de finalización de las reservas')
	
	return (True, '')

def validarHorarioReserva(inicioReserva, finalReserva, aperturaReservaEst, cierreReservaEst):
	'''
		Chequea que el horario de la reserva sea correcta considerando el horario de apertura de las reservas
		del estacionamiento.
	'''
	if inicioReserva >= finalReserva:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if finalReserva.hour - inicioReserva.hour < 1:
		return (False, 'El tiempo de reserva debe ser al menos de 1 hora')
	if finalReserva > cierreReservaEst:
		return (False, 'El horario de cierre de reserva debe estar en un horario válido')
	if inicioReserva < aperturaReservaEst:
		return (False, 'El horario de inicio de reserva debe estar en un horario válido')
	
	return (True, '')


def compararTuplasMarzullo(tupla1, tupla2):
	'Si tupla1 > tupla2 retorna 1; sino -1'
	
	if tupla1[0] > tupla2[0]: return 1
	if tupla1[0] < tupla2[0]: return -1

	if tupla1[1] >= tupla2[1]: return -1

	return 1

def interseccion(A_inicio,A_final,B_inicio,B_final):
	''' 
	    Funcion que dado dos intervalos (a1,b1),(a2,b2).
	    Indica si existe interseccion entre éllos.
    '''
	inicioMasLargo = max(A_inicio, B_inicio)
	finalMasCorto  = min(A_final, B_final)
	return inicioMasLargo < finalMasCorto


def puedeReservarALas(horaIni,horaFin,capacidad,tablaMarzullo):
	'Verifica usando Marzullo si una reserva esta disponible'
	
	tablaMarzullo.sort(key=functools.cmp_to_key(compararTuplasMarzullo))
	
	best, beststart, bestend, cnt = 0,0,0,0
	for i in range(0, len(tablaMarzullo)-1):
		cnt = cnt - tablaMarzullo[i][1]
	
		if cnt >= best:
			best, beststart  = cnt, tablaMarzullo[i][0]
			bestend = tablaMarzullo[i + 1][0]
			
		if tablaMarzullo[i][0] >= horaFin: return True
		
		if (cnt == capacidad) and \
			interseccion(horaIni, horaFin, beststart, bestend):
			return False
		
	return True
	

def crearTablaMarzullo(reservas):
	''' Funcion que dada una lista de reservaciones, devuelve 
		la tabla(lista) ordenada asociada al algoritmo de Marzullo'''
	
	listaTuplas = []
	
	for elemReserva in reservas:
		listaTuplas.append((elemReserva[0], -1))
		listaTuplas.append((elemReserva[1],  1))

	return listaTuplas

