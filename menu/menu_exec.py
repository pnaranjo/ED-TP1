#!/usr/bin/python
# Version 1
from menu import Menu
from motor.motor import Motor
from trayecto import Trayecto
import pdb
import json
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
                        if orig == dest: print ('Origen y Destino deben ser diferentes \n' + 40 * '-')

                        else:
                            dist = menu_backend.getDistance(gmaps_dict)
                            time = menu_backend.getDuration(gmaps_dict)
                            journey = Trayecto(orig, dest, dist, time)
                            journey_list.append(vars(journey))

                            print ("Origen: %s" % orig)
                            print ("Destino: %s" % dest)
                            print ("Distancia: %s" % dist)
                            print ("Duracion: %s" % time)
                            print (40 * '-')

                elif selection == '2' or selection == '02':
                        print ("2")
                elif selection == '3' or selection == '03':
                        print ("3")
                elif selection == '4' or selection == '04':
                        print ("4")
                elif selection == '5' or selection == '05':
                        print ("5")
                elif selection == '6' or selection == '06':
                        print ("6")
                elif selection == '7' or selection == '07':
                        print ("7")
                elif selection == '8' or selection == '08':
                        print ("8")
                elif selection == '9' or selection == '09':
                        #guardar con Json o similar
                        print ("9")
                elif selection == '10':
                        print ("10")
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
