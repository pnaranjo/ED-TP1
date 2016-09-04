class Menu:

    def menu():
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

         
        while True:
            try:
                for k in sorted(menu): 
                    print (str(k) + ' ' + menu[k])
                print()
                selection = input("Elija un opción: ") 
                if selection == '1': 
                    print ("1") 
                elif selection == '2':
                    print ("2")
                elif selection == '3':
                    print ("3")
                elif selection == '4':
                    print ("4")
                elif selection == '5':
                    print ("5")
                elif selection == '6':
                    print ("6")
                elif selection == '7':
                    print ("7")
                elif selection == '8':
                    print ("8")
                elif selection == '9':
                    print ("9")
                elif selection == '10':
                    print ("10")
                elif selection == '11': 
                    #llamar al metodo guardar
                    break
                else:
                    print(40 * '-')
                    print ("Opcion invalida")
                    print(40 * '-')
            except (EOFError, KeyboardInterrupt):
                print(40 * '-')
                print("comando invalido elija una de las opciones")
                print(40 * '-')
                pass
