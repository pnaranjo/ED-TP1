import json
import time

class Menu:

    def getOrigen(self,dict_gmaps):
        return dict_gmaps['origin_addresses']

    def getDestino(self,dict_gmaps):
        return dict_gmaps['destination_addresses']

    def getDuration(self,dict_gmaps):
        return dict_gmaps['rows'][0]['elements'][0]['duration']['text']

    def getDistance(self,dict_gmaps):
        return dict_gmaps['rows'][0]['elements'][0]['distance']['text']

    def guardar(self, journey_list):
        file_name = 'data-' + time.strftime("%Y-%m-%d") + '.json'
        with open(file_name, 'w') as fp:
            json.dump(journey_list, fp)
