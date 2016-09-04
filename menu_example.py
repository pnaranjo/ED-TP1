#!/usr/bin/python
# Version 1
## Show menu ##
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Crear un trayecto a partir de dos ciudades")
print ("2. Agregar una ciudad al nal de un trayecto")
print ("3. Agregar una ciudad intermedia a un trayecto")
print (30 * '-')
 
## Get input ###
choice = input('Enter your choice [1-3] : ')
 
### Convert string to int type ##
choice = int(choice)
 
### Take action as per selected menu-option ###
if choice == 1:
        print ("Crear un trayecto a partir de dos ciudades")
elif choice == 2:
        print ("Agregar una ciudad al final de un trayecto")
elif choice == 3:
        print ("Agregar una ciudad intermedia a un trayecto")
else:    ## default ##
        print ("Invalid number. Try again...")
