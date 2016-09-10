class Menu:

    def getOrigen(self,dict_gmaps):
        return dict_gmaps['origin_addresses']

    def getDestino(self,dict_gmaps):
        return dict_gmaps['destination_addresses']

    def getDuration(self,dict_gmaps):
        return dict_gmaps['rows'][0]['elements'][0]['duration']['text']

    def getDistance(self,dict_gmaps):
        return dict_gmaps['rows'][0]['elements'][0]['distance']['text']
