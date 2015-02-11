# Archivo con funciones de control para SAGE
import datetime
import functools

# Las Tuplas de cada puesto deben tener los horarios de inicio y de cierre para que
# pueda funcionar [(7:00,7:00), (19:00,19:00)]


# Suponiendo que cada estacionamiento tiene una estructura "matricial" lista de listas
# donde si m es una matriz, m[i,j] las i corresponden a los puestos y las j corresponden a tuplas
# con el horario inicio y fin de las reservas
# [[(horaIn,horaOut),(horaIn,horaOut)],[],....]

# chequeo de horarios de extended
def HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin):

	if HoraInicio >= HoraFin:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if ReservaInicio >= ReservaFin:
		return (False, 'El horario de inicio de reserva debe ser menor al horario de cierre')
	if ReservaInicio < HoraInicio:
		return (False, 'El horario de inicio de reserva debe mayor o igual al horario de apertura del estacionamiento')
	if ReservaInicio > HoraFin:
		return (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento')
	if ReservaFin < HoraInicio:
		return (False, 'El horario de apertura de estacionamiento debe ser menor al horario de finalización de reservas')
	if ReservaFin > HoraFin:
		return (False, 'El horario de cierre de estacionamiento debe ser mayor o igual al horario de finalización de reservas')
	return (True, '')

def validarHorarioReserva(ReservaInicio, ReservaFin, HorarioApertura, HorarioCierre):

	if ReservaInicio >= ReservaFin:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if ReservaFin.hour - ReservaInicio.hour < 1:
		return (False, 'El tiempo de reserva debe ser al menos de 1 hora')
	if ReservaFin > HorarioCierre:
		return (False, 'El horario de inicio de reserva debe estar en un horario válido')
	if ReservaInicio < HorarioApertura:
		return (False, 'El horario de cierre de reserva debe estar en un horario válido')
	return (True, '')


def compararTuplasMarzullo(tupla1, tupla2):
	'''Organiza las tuplas primero por offset y luego por tipo
       Reglas: en resumen si x > y, se debe retornar 1; si y > x, se debe retornar -1
    '''
	
	if tupla1[0] > tupla2[0]: return 1
	if tupla1[0] < tupla2[0]: return -1

	if tupla1[0] == tupla2[0]:
		if tupla1[1] >= tupla2[1]:
			return -1
		return 1

def interseccion(A_inicio,A_final,B_inicio,B_final):
	''' 
    Funcion que Dado dos intervalos (a1,b1),(a2,b2)
    Indica si existe interseccion entre ellas
    '''
	inicioMasLargo = max(A_inicio, B_inicio)
	finalMasCorto = min(A_final, B_final)
	return inicioMasLargo < finalMasCorto


def puedeReservarALas(horaIni,horaFin,capacidad,tablaMarzullo):
	'Verifica usando Marzullo si una reserva esta disponible'
	
	puestosOcupados =  [-1]
	
	best, beststart, bestend, cnt = 0,0,0,0
	for i in range(0, len(tablaMarzullo)-1):
		cnt = cnt - tablaMarzullo[i][1]
	
		if cnt >= best:
			best, beststart  = cnt, tablaMarzullo[i][0]
			bestend = tablaMarzullo[i + 1][0]
			
			if interseccion(horaIni, horaFin, beststart, bestend):
				puestosOcupados.append(tablaMarzullo[i][2])
		
		if tablaMarzullo[i][0] >= horaFin: return puestosOcupados
		
		if (cnt == capacidad) and \
			interseccion(horaIni, horaFin, beststart, bestend):
			return []
		
	return puestosOcupados
	

def crearTablaMarzullo(puestos):
	''' Funcion que dada una lista de reservaciones, devuelve 
		la tabla(lista) ordenada asociada al algoritmo de Marzullo'''
	
	listaTuplas = []
	
	for puesto in puestos:
		tuplaIni = (puesto[1], -1, puesto[0])
		tuplaFin = (puesto[2],  1, puesto[0])
		listaTuplas.append(tuplaIni)
		listaTuplas.append(tuplaFin)

	#===========================================================================
	# '''Funcion que dada una tupla (offset,type) ordena por offset y en
	# caso de ser iguales, ordena por type (-1 tiene mayor precedencia)
	# ejmp: [(5,1),(8,1),(8,-1)] -> [(5,1),(8,-1),(8,1)]'''
	# listaTuplas.sort(key=functools.cmp_to_key(compararTuplasMarzullo))
	#===========================================================================

	return listaTuplas
	
#===============================================================================
# # inserta ordenadamente por hora de inicio
# def insertarReserva(hin, hout, puesto, listaReserva):
# 	# no verifica precondicion, se supone que se hace buscar antes para ver si se puede agregar
# 	if not isinstance(listaReserva, list):
# 		return None
# 	if len(listaReserva) == 0:
# 		return listaReserva
# 	if not isinstance(hin, datetime.time) or not isinstance(hout, datetime.time):
# 		return listaReserva
# 	tupla = (hin, hout)
# 	listaReserva.insert(puesto, tupla)
# 	# estacionamiento[puesto].sort()
# 	return listaReserva
#===============================================================================

#===============================================================================
# def reservar(self,horaIni,horaFin , puesto):
# 	
# 	#No refactorizar aunque se vea que se puede xD , solo quitaria claridad.
# 	if self.reserva_disponible(horaIni, horaFin):
# 		self.listaReservas.append((horaIni , horaFin))
# 		self.recrear_tabla = True
# 		return True
# 
# 	return False
#===============================================================================

