# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts       import render , redirect
from decimal import Decimal
from estacionamientos.controller import *
from estacionamientos.forms      import EstacionamientoExtendedForm, DefinirTarifa
from estacionamientos.forms      import EstacionamientoForm
from estacionamientos.forms      import EstacionamientoReserva
from estacionamientos.models     import Estacionamiento, ReservasModel 
from django.core.context_processors import request

datosReservaActual = (-1,-1)

# Usamos esta vista para procesar todos los estacionamientos
def estacionamientos_all(request):
    # Si se hace un POST a esta vista implica que se quiere agregar un nuevo
    # estacionamiento
    estacionamientos = Estacionamiento.objects.all()
    
    if request.method == 'POST':
            # Creamos un formulario con los datos que recibimos
            form = EstacionamientoForm(request.POST)

            # Parte de la entrega era limitar la cantidad maxima de
            # estacionamientos a 5
            if len(estacionamientos) >= 5:
                context = {'color':'red', 
                           'mensaje':'No se pueden agregar más estacionamientos'}
                return render(request, 'templateMensaje.html', context)

            # Si el formulario es valido, entonces creamos un objeto con
            # el constructor del modelo
            if form.is_valid():
                obj = Estacionamiento(
                        Propietario = form.cleaned_data['propietario'],
                        Nombre = form.cleaned_data['nombre'],
                        Direccion = form.cleaned_data['direccion'],
                        Rif = form.cleaned_data['rif'],
                        Telefono_1 = form.cleaned_data['telefono_1'],
                        Telefono_2 = form.cleaned_data['telefono_2'],
                        Telefono_3 = form.cleaned_data['telefono_3'],
                        Email_1 = form.cleaned_data['email_1'],
                        Email_2 = form.cleaned_data['email_2']
                )
                obj.save()
                # Recargamos los estacionamientos ya que acabamos de agregar
                estacionamientos = Estacionamiento.objects.all()
    # Si no es un POST es un GET, y mandamos un formulario vacio
    else:
        form = EstacionamientoForm()
        
    context = {'form': form, 
               'estacionamientos': estacionamientos}
    return render(request, 'base.html', context)

def estacionamiento_detail(request, _id):

    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacion = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        return render(request, '404.html')

    if request.method == 'POST':
            # Leemos el formulario
            form = EstacionamientoExtendedForm(request.POST)
            
            # Si el formulario
            if form.is_valid():
                hora_in = form.cleaned_data['Apertura']
                hora_out = form.cleaned_data['Cierre']
                reserva_in = form.cleaned_data['Reservas_Inicio']
                reserva_out = form.cleaned_data['Reservas_Cierre']

                m_validado = validarHorarioEstacionamiento(hora_in, hora_out, reserva_in, reserva_out)
                if not m_validado[0]:
                    context = {'color':'red', 
                               'mensaje': m_validado[1]}
                    return render(request, 'templateMensaje.html', context)

                estacion.Tarifa = form.cleaned_data['Tarifa']
                estacion.Apertura = hora_in
                estacion.Cierre = hora_out
                estacion.Reservas_Inicio = reserva_in
                estacion.Reservas_Cierre = reserva_out
                estacion.NroPuesto = form.cleaned_data['NroPuesto']
                
                estacion.Tarifa.tarifa = Decimal(form.cleaned_data['monto'])
                estacion.save()
                estacion.Tarifa.save()
                
    else:
        form = EstacionamientoExtendedForm()

    return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacion})

def estacionamiento_confirmar_reserva(request,id_est):
    #global datosReservaActual

    id_est = int(id_est)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacion = Estacionamiento.objects.get(id = id_est)
    except ObjectDoesNotExist:
        return render(request, '404.html')

    # Si se hace un GET renderizamos los estacionamientos con su formulario
    if request.method == 'GET': return redirect('./reserva', _id=str(id_est))

    # Si es un POST estan mandando un request
    if request.method == 'POST':        
        form = EstacionamientoReserva(request.POST)         
        if form.is_valid():
            inicio_reserva = form.cleaned_data['inicio']
            final_reserva  = form.cleaned_data['final']
            
            reservado = ReservasModel(
                Estacionamiento = estacion,
                InicioReserva = inicio_reserva,
                FinalReserva = final_reserva
            )
            
            reservado.save() 
        return redirect('./reserva', _id=str(id_est))
        
    return redirect('./reserva', _id=str(id_est))

def estacionamiento_reserva(request, _id):

    _id = int(_id)
    # Verificamos que el objeto exista antes de continuar
    try:
        estacion = Estacionamiento.objects.get(id = _id)
    except ObjectDoesNotExist:
        return render(request, '404.html')

    # Si se hace un GET renderizamos los estacionamientos con su formulario
    if request.method == 'GET':
        form = EstacionamientoReserva()
        context = {'form': form, 
                   'estacionamiento': estacion}
        return render(request, 'estacionamientoReserva.html', context)

    # Si es un POST estan mandando un request
    if request.method == 'POST':
        
            form = EstacionamientoReserva(request.POST)
            if form.is_valid():
                inicio_reserva = form.cleaned_data['inicio']
                final_reserva  = form.cleaned_data['final']

                # Validamos los horarios con los horario de salida y entrada
                m_validado = validarHorarioReserva(inicio_reserva, final_reserva, estacion.Reservas_Inicio, estacion.Reservas_Cierre)
                horario_aceptado = m_validado[0]
                
                # Si no es valido devolvemos el request
                if not horario_aceptado:
                    context = {'color':'red', 
                               'mensaje': m_validado[1]}
                    return render(request, 'templateMensaje.html', context)

                #Obtiene las reservas creadas para el estacionamiento con id igual a '_id'
                reservas = ReservasModel.objects.filter(Estacionamiento = estacion)
                #Obtiene los valores que interesan de cada reserva en forma de una tupla
                reservas = reservas.values_list('InicioReserva', 'FinalReserva')
                           
                if puedeReservarALas(inicio_reserva, final_reserva,\
                                estacion.NroPuesto,reservas):

                    precio = calculoPrecio(inicio_reserva, final_reserva, estacion.Tarifa)
                    int_precio = precio.to_integral_value()
                    if precio == int_precio:
                        precio = int_precio
                        
                    duracion = calcularDuracion(inicio_reserva, final_reserva)
                    cad_duracion = cadena_duracion(*duracion)
                    context = {'color':'green',
                                    'hora_inicio': str(inicio_reserva),
                                    'hora_final': str(final_reserva),
                                    'id':_id,
                                    'precio' : precio,
                                    'mensaje':'Reserva disponible!',
                                    'color':'green',
                                    'duracion':cad_duracion,
                                   }
                    return render(request, 'estacionamientoConfirReserva.html', context)
                
                else:
                    context = {'color':'red',
                               'hora_inicio': str(inicio_reserva),
                               'hora_final': str(final_reserva),
                               'id':_id,
                                'mensaje':'Reserva no disponible!',
                               }
                    
                    return render(request, 'estacionamientoConfirReserva.html', context)
                
    form = EstacionamientoReserva()
    context = {'form': form, 
               'estacionamiento': estacion}

    return render(request, 'estacionamientoReserva.html', context)

