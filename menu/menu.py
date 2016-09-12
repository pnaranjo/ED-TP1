import json
import time
import pprint

class Menu:

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

    def guardar(self, journey_list):
        file_name = 'data-' + time.strftime("%Y-%m-%d") + '.json'
        with open(file_name, 'w') as fp:
            json.dump(journey_list, fp)

    def get_trayecto(self, journey_list, journey_id):
        resp = None
        for journey in journey_list:
            if journey['id'] == journey_id: resp = journey
        return resp


    def listar(self, journey_list):
        for journey in journey_list:
            pprint.pprint(journey)
            print ( 40 * "-" )
