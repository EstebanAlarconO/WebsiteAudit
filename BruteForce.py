from functions import *

flag = True
correo = ''
pw =''
while(flag):
    print("Bienvenido!!\n")
    print("Seleccione una opcion\n")
    print("1) Crear cuenta\n2) Inicio Sesión\n3) Reestablecer contraseña\n4) Modificar contraseña\n5) Realizar ataque\n6) Salir\n")
    opcion = input()
    if(opcion == '1'):
        print("Su contraseña se creará de forma aleatoria")
        correo = input("\nIngrese el correo de usuario:\n")
        pagina = input("1) spider.cl\n2) atmosferasport.es\n")
        if (pagina == '1'):
            correo, pw = registro_spider(correo)

        elif(pagina == '2'):
            correo, pw = registro_atmosferasport(correo)

        else:
            print("Opcion invalida")
            continue
    elif(opcion == '2'):
        pagina = input("1) spider.cl\n2) atmosferasport.es\n")
        if(correo == '' and pw == ''):
            correo = input("\nIngrese el correo de usuario:\n")
            pw = input("\nIngrese contraseña:\n")
        elif(correo != '' and pw == ''):
            pw = input("\nIngrese contraseña:\n")
        elif(correo == '' and pw != ''):
            correo = input("\nIngrese el correo de usuario:\n")
        
        if (pagina == '1'):
            inicio_spider(correo, pw)

        elif(pagina == '2'):
            inicio_atmosferasport(correo,pw)
            continue
        else:
            print("Opcion invalida")
            continue

    elif(opcion == '3'):
        if(correo == ''):
            correo = input("\nIngrese el correo de usuario:\n")

        pagina = input("1) spider.cl\n2) atmosferasport.es\n")
        if (pagina == '1'):
            reestablecer_spider(correo, pw)

        elif(pagina == '2'):
            #reestablecer_atmosferasport(correo,intentos)
            continue
        else:
            print("Opcion invalida")
            continue

    elif(opcion == '4'):
        pagina = input("1) spider.cl\n2) atmosferasport.es\n")
        if(correo == '' and pw == ''):
            correo = input("\nIngrese el correo de usuario:\n")
            pw = input("\nIngrese contraseña:\n")
        elif(correo != '' and pw == ''):
            pw = input("\nIngrese contraseña:\n")
        elif(correo == '' and pw != ''):
            correo = input("\nIngrese el correo de usuario:\n")
        
        if (pagina == '1'):
            cambiarPW_spider(correo, pw)

        elif(pagina == '2'):
            print("Su nueva contraseña es: ", cambiarPW_atmosferasport(correo,pw))

        else:
            print("Opcion invalida")
            continue

    elif(opcion == '5'):
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
        
    elif(opcion == '6'):
        try:
            driver.quit()
            flag = False
        except:
            flag = False
    else:
        print("Seleccione una opcion valida\n")
