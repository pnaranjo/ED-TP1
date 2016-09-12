import uuid

class Trayecto(object):
    """docstring for ."""
    def __init__(self, origen, destino, distancia, tiempo, name=None ,time_in_sec=0):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.tiempo = tiempo
        self.name = name
        self.id = str(uuid.uuid4())
        self.time_in_sec = time_in_sec
