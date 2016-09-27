#!/usr/bin/python
# Version 1
from menu import Menu
from motor.motor import Motor
from trayecto import Trayecto
import googlemaps
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
                     origen = input("Ciudad Origen: ")
                     destino = input("Ciudad Destino: ")
                     journey_name = input('Elija un nombre para su trayecto: ')
                     journey = menu_backend.create_trayecto(origen,destino,journey_name)
                     if journey:
                         menu_backend.print_trayecto(journey)
                         journey_list.append(vars(journey))

                elif selection == '2' or selection == '02':
                     menu_backend.listar(journey_list)
                     print (40 * '-')
                     journey_id = input('Ingrese el ID del trayecto que desea utilizar: ')
                     trayecto = menu_backend.get_trayecto(journey_list, journey_id)
                     if not trayecto: continue
                     new_dest = input('Ingrese el nuevo destino: ')
                     journey_name = input('Elija un nombre para su trayecto: ')
                     journey = menu_backend.add_destination(trayecto, new_dest, journey_name)
                     if journey:
                         menu_backend.print_trayecto(journey)
                         journey_list.append(vars(journey))

                elif selection == '3' or selection == '03':
                     menu_backend.listar(journey_list)
                     print (40 * '-')
                     journey_id = input('Ingrese el ID del trayecto que desea utilizar: ')
                     trayecto = menu_backend.get_trayecto(journey_list, journey_id)
                     if not trayecto: continue
                     ciudades = menu_backend.getCiudades(trayecto)
                     menu_backend.print_ciudades(ciudades)
                     ciudad_elec = input('Ingrese el numero de ciudad. El nuevo destino sera insertado previo a esa ciudad:  ')
                     if ciudad_elec not in ciudades.keys():
                         input ('Numero ingresado invalido')
                         continue
                     ciudad_perteneciente = ciudades[ciudad_elec]
                     ciudad_intermedia = input('Ingrese el destino intermedio: ')
                     journey_name = input('Elija un nombre para su trayecto: ')
                     journey = menu_backend.add_intermediate(trayecto, ciudad_intermedia, ciudad_perteneciente, journey_name)
                     if journey:
                         menu_backend.print_trayecto(journey)
                         journey_list.append(vars(journey))

                elif selection == '4' or selection == '04':
                     menu_backend.listar(journey_list)
                     print (40 * '-')
                     journey_id1 = input('Ingrese el ID del primer trayecto que desea utilizar: ')
                     trayecto1 = menu_backend.get_trayecto(journey_list, journey_id1)
                     if not trayecto1: continue
                     journey_id2 = input('Ingrese el ID del segundo trayecto que desea utilizar: ')
                     trayecto2 = menu_backend.get_trayecto(journey_list, journey_id2)
                     if not trayecto2: continue
                     journey_name = input('Elija un nombre para su trayecto: ')
                     journey = menu_backend.join_journey(trayecto1,trayecto2,journey_name)
                     if journey:
                         menu_backend.print_trayecto(journey)
                         journey_list.append(vars(journey))
                     
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
                        menu_backend.listar(journey_list)
                        print ('\n')
                        journey_id = input('Ingrese el ID del trayecto que desea utilizar: ')
                        journey = menu_backend.get_trayecto(journey_list, journey_id)

                        # obtengo la lista de origenes y destinos
                        destino_list = []
                        origen_list = []
                        for k, v in journey.items():
                            if k == 'origen':
                                origen_list.append(v)
                                print('origen_list ', origen_list)
                            if k == 'destino':
                                destino_list.append(v)
                                print('destino_list ', destino_list)
                        # recorro las listas y voy armando los trayectos
                        for x in origen_list:
                            print(x)
                            origen = x
                            for y in destino_list:
                                print(y)
                                destino = y
                                print(origen, ' - ', destino)
                                gmaps_dict = gm.create_trayecto(origen,destino)
                                print ('Tiempo', menu_backend.getDuration(gmaps_dict))
                                print ('Distancia', menu_backend.getDistance(gmaps_dict))
                                print(40 * '-')
                        input('Presione Enter para continuar...')
                elif selection == '8' or selection == '08':
                        print (40 * '-')
                        menu_backend.listar(journey_list)
                        input('Presione Enter para continuar...')
                elif selection == '9' or selection == '09':
                        file_name=input('Guardar... escriba el nombre del archivo:')
                        file_name=file_name.replace(' ', '') + '.json'
                        menu_backend.guardar(journey_list, file_name)
                elif selection == '10':
                        json_file = input('nombre del archivo: ')
                        try:
                            menu_backend.cargar(json_file, journey_list)
                            print('Archivo %s cargado satisfactoriamente...' % json_file)
                            input('Presione Enter para continuar...')
                        except (Exception):
                            input('Archivo no encontrado... Presione ENTER para continuar')
                            continue


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
