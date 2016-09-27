import json
import time
import pprint
import pdb
from motor.motor import Motor
from trayecto import Trayecto
from exceptions import CustomException

import json
import pprint
import os

class Menu:
    def __init__(self):
        self.motor = Motor()

    def getOrigen(self,dict_gmaps):
        return dict_gmaps['origin_addresses']

    def getDestino(self,dict_gmaps):
        return dict_gmaps['destination_addresses']

    def getDuration(self,dict_gmaps):
        return dict_gmaps['rows'][0]['elements'][0]['duration']['text']

    def getTimeInSec(self,dict_gmaps):
        return dict_gmaps['rows'][0]['elements'][0]['duration']['value']

    def getDistance(self,dict_gmaps):
        return dict_gmaps['rows'][0]['elements'][0]['distance']['text']

    def guardar(self, journey_list, file_name='data-' + time.strftime("%Y-%m-%d") + '.json'):
        with open(file_name, 'w') as fp:
            json.dump(journey_list, fp)

    def getStatus(self,dict_gmaps):
        return dict_gmaps['rows'][0]['elements'][0]['status']

    def get_trayecto(self, journey_list, journey_id):
        resp = None
        try:
            for journey in journey_list:
                if journey['id'] == journey_id: resp = journey
            if not resp: raise Exception
            else: return resp
        except(Exception):
            input('id no encontrado')
            return None

    def listar(self, journey_list):
        for journey in journey_list:
            pprint.pprint(journey)
            print ( 40 * "-" )

    def cargar(self, archivo, journey_list):
        with open(archivo) as json_file:
            json_data = json.load(json_file)
            for j in json_data:
                journey_list.append(j)
            print(journey_list)

    def print_trayecto(self, trayecto):
        print (40 * '-')
        print ('Nombre: %s' % trayecto.name)
        print ('Origen: %s' % trayecto.origen)
        print ('Destino: %s' % trayecto.destino)
        print ('Distancia %s' % trayecto.distancia)
        print ('Tiempo %s' % trayecto.tiempo)
        input ('Presion Enter para continuar...')
        print (40 * '-')

    def getCiudades(self, trayecto):
        ciudades = {}
        ciudades['1'] = trayecto['origen']
        i = 2
        for d in trayecto['destino']:
            ciudades[str(i)] = d
            i += 1
        return ciudades

    def print_ciudades(self,ciudades):
        keys = ciudades.keys()
        print('Ciudades del trayecto')
        print (40 * '-')
        for key in sorted(keys):
            print('[' + key + ']' + ' ' + ciudades[key])

    def create_trayecto(self, origen, destino, name):
        try:
            tray = self.motor.create_trayecto(origen,destino)
            if self.getOrigen(tray) == self.getDestino(tray) or self.getStatus(tray) != 'OK': raise CustomException
        except (CustomException):
            input('No es posible calcular la distancia... Presione Enter')
            return None
        return Trayecto(self.getOrigen(tray)[0],self.getDestino(tray),self.getDistance(tray),
                            self.getDuration(tray), name, self.getTimeInSec(tray))

    def add_destination(self, trayecto, new_dest, name):
        origen = trayecto['origen']
        initial_dest = trayecto['destino']
        destino = initial_dest[-1]
        tray_1 = self.create_trayecto(destino,new_dest,name)
        if not tray_1: return None
        try:
            if tray_1.destino[0] == destino: raise Exception
        except (Exception):
            input('El nuevo destino tiene que ser diferente al destino original...')
            return None
        dest=[]
        for d in initial_dest: dest.append(d)
        dest.append(tray_1.destino[0])
        dist = str(int(trayecto['distancia'].split(' ')[0].replace(",","")) + int(tray_1.distancia.split(' ')[0].replace(",",""))) + ' km'
        time_in_sec = trayecto['time_in_sec'] + tray_1.time_in_sec
        time = self.time_in_sec_to_time(time_in_sec)
        return Trayecto(origen,dest,dist,time,name,time_in_sec)

    def add_intermediate(self, trayecto, ciudad, ciudad_perteneciente, name):
        if ciudad_perteneciente == trayecto['origen']:
            origen = ciudad
            tray_1 = self.create_trayecto(origen,ciudad_perteneciente,name)
            dest = []
            dest.append(ciudad_perteneciente)
            for d in trayecto['destino']: dest.append(d)
            dist = str(int(trayecto['distancia'].split(' ')[0].replace(",","")) + int(tray_1.distancia.split(' ')[0].replace(",",""))) + ' km'
            time_in_sec = trayecto['time_in_sec'] + tray_1.time_in_sec
            return Trayecto(tray_1.origen,dest,dist,time,name,time_in_sec)
        else:
            origen = trayecto['origen']
            dest = []
            for c in trayecto['destino']:
                if c != ciudad_perteneciente: dest.append(c)
                else:
                    dest.append(ciudad)
                    dest.append(c)
            tray_1 = self.create_trayecto(origen,dest[0],'tray-temp')
            for d in range(1,len(dest)):
                tray_1 = self.add_destination(vars(tray_1), dest[d], name)
            return tray_1

    def join_journey(self, trayecto1, trayecto2, name):
        origen = trayecto1['origen']
        dest = []
        for d in trayecto1['destino']: dest.append(d)
        if trayecto1['destino'][-1] != trayecto2['origen']:
            dest.append(trayecto2['origen'])
        for d in trayecto2['destino']: dest.append(d)
        tray = self.create_trayecto(origen,dest[0],'tray-temp')
        for d in range(1,len(dest)):
            tray = self.add_destination(vars(tray), dest[d], name)
        return tray

    def time_in_sec_to_time(self, time_in_sec):
        time_in_hours=int(time_in_sec/60/60)
        time_in_min=round((time_in_sec/60/60)%1 * 60)
        if time_in_hours == 0 : return (str(time_in_min) + ' mins')
        else:
            return (str(time_in_hours) + ' hours, ' + str(time_in_min) + ' mins')
