#!/usr/bin/python
# Version 1
from menu import Menu
from motor.motor import Motor
from trayecto import Trayecto
import pdb
import json
import pprint
import os
## Show menu ##

menu = {}
menu['01']="Crear un trayecto a partir de dos ciudades"
menu['02']="Agregar una ciudad al final de un trayecto"
menu['03']="Agregar una ciudad intermedia a un trayecto"
menu['04']="Concatenar dos trayectos"
menu['05']="Comparar dos trayectos"
menu['06']="Mostrar un trayecto"
menu['07']="Mostrar rutas"
menu['08']="Listar los trayectos calculados"
menu['09']="Almacenar en disco los trayectos calculados"
menu['10']="Recuperar de disco los trayectos alamcenados"
menu['11']="Salir del sistema"

gm = Motor()
menu_backend = Menu()

journey_list = []

while True:
        try:
                os.system('clear')
                for k in sorted(menu):
                        print (str(k) + ' ' + menu[k])
                print()
                selection = input("Elija un opción: ")

                if selection == '1' or selection == '01':

                        print (menu['01'])
                        origen = input("Ciudad Origen: ")
                        destino = input("Ciudad Destino: ")

                        print (40 * '-')
                        gmaps_dict = gm.create_trayecto(origen,destino)
                        orig = menu_backend.getOrigen(gmaps_dict)[0]
                        dest = menu_backend.getDestino(gmaps_dict)[0]
                        while orig == dest:
                            print('Origen y Destino deben ser diferentes \n' + 40 * '-')
                            origen = input("Ciudad Origen: ")
                            destino = input("Ciudad Destino: ")

                        if gmaps_dict['rows'][0]['elements'][0]['status'] != 'OK':
                            print ('No es posible calcular el trayecto entre las ciudades " %s " y " %s "' % (orig,dest))
                            print ( 40 * '-' )
                            input('Presione Enter para continuar...')
                        else:
                            journey_name = input('Elija un nombre para su trayecto: ')
                            print (40 * '-')
                            dist = menu_backend.getDistance(gmaps_dict)
                            time = menu_backend.getDuration(gmaps_dict)
                            time_in_sec = menu_backend.getTimeInSec(gmaps_dict)
                            journey = Trayecto(orig, dest, dist, time, journey_name, time_in_sec)
                            journey_list.append(vars(journey))

                            print ("Origen: %s" % orig)
                            print ("Destino: %s" % dest)
                            print ("Distancia: %s" % dist)
                            print ("Duracion: %s" % time)
                            print (40 * '-')
                            input('Presione Enter para continuar...')

                elif selection == '2' or selection == '02':
                        print (40 * '-')
                        menu_backend.listar(journey_list)
                        print ('\n')
                        journey_id = input('Ingrese el ID del trayecto que desea utilizar: ')
                        journey_orig = menu_backend.get_trayecto(journey_list, journey_id)
                        origen = journey_orig['destino']
                        destino = input('Ingrese el nuevo destino: ')
                        gmaps_dict = gm.create_trayecto(origen,destino)
                        while menu_backend.getDestino(gmaps_dict)[0] == journey_orig['destino']: destino = input('Los destinos son iguales... Ingrese el nuevo destino: ')
                        gmaps_dict = gm.create_trayecto(origen,destino)
                        #pdb.set_trace()
                        journey_name = input('Elija un nombre para su trayecto: ')
                        print (40 * '-')
                        orig = journey_orig['origen']
                        dest = []
                        dest.append(journey_orig['destino'])
                        dest.append(menu_backend.getDestino(gmaps_dict)[0])
                        dist = str(float( journey_orig['distancia'].split(' ')[0].replace(',','') ) + float(menu_backend.getDistance(gmaps_dict).split(' ')[0].replace(',',''))) + ' km'
                        time_in_sec = menu_backend.getTimeInSec(gmaps_dict) + journey_orig['time_in_sec']
                        time = time_in_sec_to_time(time_in_sec)
                        journey = Trayecto(orig, dest, dist, time, journey_name, time_in_sec)
                        journey_list.append(vars(journey))

                        print ("Origen: %s" % orig)
                        print ("Destino: %s" % dest)
                        print ("Distancia: %s" % dist)
                        print ("Duracion: %s" % time)
                        print (40 * '-')
                        input('Presione Enter para continuar...')

                elif selection == '3' or selection == '03':
                        print ("3")
                elif selection == '4' or selection == '04':
                        print ("4")
                elif selection == '5' or selection == '05':
                        #Comparar dos trayectos d para distancia t para tiempo
                        tipo_comp = input('comparar por d -> distacia, t -> tiempo: ' )
                        if tipo_comp != 'd' and tipo_comp != 't':
                            print ('los valores validos son d o t')
                            print(40 * '-')
                            input('Presione Enter para continuar...')
                        else:
                            menu_backend.listar(journey_list)
                            print ('\n')
                            journey_id_p = input('Ingrese el ID del primer trayecto que desea utilizar: ')
                            journey_id_s = input('Ingrese el ID del segundo trayecto que desea utilizar: ')
                            if str(tipo_comp) == 'd':
                                #decir el trayecto con mayor distacia es
                                journey_p = menu_backend.get_trayecto(journey_list, journey_id_p)
                                primero = journey_p['distancia']
                                primero_number = primero.split(' ')[0]
                                primero_number.replace(',','')

                                journey_s = menu_backend.get_trayecto(journey_list, journey_id_s)
                                segundo = journey_s['distancia']
                                segundo_number = segundo.split(' ')[0]
                                segundo_number = str(segundo_number.replace(',',''))

                                t1 = float(primero_number)
                                t2 = float(segundo_number)

                                if t1 > t2:
                                    print('Trayecto uno recorrio mas distancia')
                                elif t1 < t2:
                                    print('Trayecto dos recorrio mas distancia')
                                else:
                                    print('ambos recorrieron misma distancia')
                                print(40 * '-')
                                input('Presione Enter para continuar...')
                            else:
                                #decir el trayecto con mayor tiempo es
                                journey_p = menu_backend.get_trayecto(journey_list, journey_id_p)
                                primero = journey_p['time_in_sec']

                                journey_s = menu_backend.get_trayecto(journey_list, journey_id_s)
                                segundo = journey_s['time_in_sec']

                                if primero > segundo:
                                    print('Trayecto uno viajo mas tiempo')
                                elif primero < segundo:
                                    print('Trayecto dos viajo mas tiempo')
                                else:
                                    print('ambos viajaron misma cantidad de tiempo')

                                print(40 * '-')
                                input('Presione Enter para continuar...')
                elif selection == '6' or selection == '06':
                        menu_backend.listar(journey_list)
                        print ('\n')
                        journey_id = input('Ingrese el ID del primer trayecto que desea utilizar: ')
                        journey = menu_backend.get_trayecto(journey_list, journey_id)
                        #limpio origen
                        origen_str = str(journey['origen']).replace("'",'')
                        origen_str = origen_str.replace("[",' ')
                        origen_str = origen_str.replace("]",' ')
                        #limpio destino
                        destino_str = str(journey['destino']).replace("'",'')
                        destino_str = destino_str.replace("[",' ')
                        destino_str = destino_str.replace("]",' ')

                        pprint.pprint('Ciudades: ' + origen_str + ', ' + destino_str)
                        pprint.pprint('Distancia ' + journey['distancia'])
                        pprint.pprint('Tiempo ' + journey['tiempo'])

                        print(40 * '-')
                        input('Presione Enter para continuar...')

                elif selection == '7' or selection == '07':
                        print ("7")
                elif selection == '8' or selection == '08':
                        print (40 * '-')
                        menu_backend.listar(journey_list)
                        input('Presione Enter para continuar...')
                elif selection == '9' or selection == '09':
                        menu_backend.guardar(journey_list)
                elif selection == '10':
                        menu_backend.cargar(input('nombre del archivo: '))
                        input('Presione Enter para continuar...')
                elif selection == '11':
                        menu_backend.guardar(journey_list)
                        break
                else:
                        print(40 * '-')
                        print ("Opcion invalida")
                        print(40 * '-')
        except (EOFError, KeyboardInterrupt):
                print(40 * '-')
                print ("Para Salir elija la opcion 11")
                print(40 * '-')

        def time_in_sec_to_time(time_in_sec):
            time_in_hours=int(time_in_sec/60/60)
            time_in_min=round((time_in_sec/60)%1 * 60)
            if time_in_hours == 0 : return (str(time_in_min) + ' mins')
            else:
                return (str(time_in_hours) + ' hours, ' + str(time_in_min) + ' mins')
