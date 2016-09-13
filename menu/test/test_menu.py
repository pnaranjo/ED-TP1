import unittest
from menu import Menu
from motor.motor import Motor
from trayecto import Trayecto
import pdb

ciudad1 = 'Buenos Aires'
ciudad2 = 'Bs As'
ciudad3 = 'Rosario'
ciudad4 = 'Cordoba'

menu_backend = Menu()
motor = Motor()

class MenuTest(unittest.TestCase):
    def test_crear_trayecto_1(self):
        trayecto = motor.create_trayecto(ciudad1,ciudad2)
        orig = menu_backend.getOrigen(trayecto)[0]
        dest = menu_backend.getDestino(trayecto)[0]
        dist = menu_backend.getDistance(trayecto)
        time = menu_backend.getDuration(trayecto)
        time_in_sec = menu_backend.getTimeInSec(trayecto)
        journey = Trayecto(orig, dest, dist, time, time_in_sec, 'trayecto_test')
        haskeys = 'origen' in vars(journey)
        haskeys = haskeys and 'destino' in vars(journey)
        haskeys = haskeys and 'distancia' in vars(journey)
        haskeys = haskeys and 'tiempo' in vars(journey)
        haskeys = haskeys and 'name' in vars(journey)
        haskeys = haskeys and 'id' in vars(journey)
        assert haskeys

    
