#! /usr/bin/env python
# coding: utf8

from config import *
import googlemaps


if __name__ == '__main__':
    ciudad1 = 'Buenos Aires'
    ciudad2 = 'Cordoba'
    ciudad3 = 'Tokio'
    ciudad4 = 'Casasasasa'

    gmaps=googlemaps.Client(key=KEY) #inicializa la aplicación para consultar
                                     # los mapas de google
    ruta1 = gmaps.distance_matrix(ciudad1, ciudad2)
    ruta2 = gmaps.distance_matrix(ciudad2, ciudad3)
    ruta3 = gmaps.distance_matrix(ciudad3, ciudad4)

    

    rutas = {'ruta1':ruta1, 'ruta2':ruta2, 'ruta3':ruta3}

    for k, v in rutas.items():
        
        if v['rows'][0]['elements'][0]['status'] == 'OK':
            d1 = v['rows'][0]['elements'][0]['distance']['value']
            t1 = v['rows'][0]['elements'][0]['duration']['value']
            dias1=int(t1/24/60/60)
            t1=t1-dias1*24*60*60
            horas1=int(t1/60/60)
            t1=t1-horas1*60*60
            min1=int(t1/60)
           
            print("Distancia " + k +  ": " + v['rows'][0]['elements'][0]['distance']['text'])
            print("Tiempo estimado: {0:2d} dias, {1:2d} horas, {2:2d} min".format(dias1, horas1, min1))
            print( k , v,'\n')

        else:
            print('Error en ' + k + ': ' + v['rows'][0]['elements'][0]['status'] )
            print( k , v,'\n')
    
  
