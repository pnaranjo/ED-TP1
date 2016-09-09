from .config import *
import googlemaps

class Motor(object):
    """docstring for Motor."""
    def __init__(self):
        self.gmaps = googlemaps.Client(key=KEY)

    def get_trayecto(self, origen, destino):
        ruta = self.gmaps.distance_matrix(origen,destino)
        return ruta
