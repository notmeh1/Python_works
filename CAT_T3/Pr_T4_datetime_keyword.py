from datetime import date, datetime, time
import keyword

loop = True
while loop:
    print("1.- Modulo de keyword")
    print("2.- Modulo de datetime")
    menuSelection = input("Ingrese el numero del modulo que quiera ingresar...")
    if menuSelection == "1":
        while loop:
            print("1.- Check de keyword y softword")
            print("2.- Listados de keyword y softword")
            print("3.- Volver")
            menuSelection = input("Ingrese el numero del programa que quiera ingresar...")
            if menuSelection == "1":
                inputList = []
                while loop:
                    print('--------------------------------' * 2)
                    userInput = input("Escriba algo... ")

                    # Retorna un boolean si el string indicado es igual a alguna keyword
                    keyCheck = 'Si' if keyword.iskeyword(userInput) else 'No'
                    # Retorna un boolean si el string indicado es igual a alguna softword
                    softCheck = 'Si' if keyword.issoftkeyword(userInput) else 'No'
                    item = {
                        'Entrada del usuario': userInput,
                        'Contiene alguna keyword?': keyCheck,
                        'Contiene alguna softword?': softCheck
                    }
                    inputList.append(item)
                    for item in inputList:
                        print(item)
            elif menuSelection == "2":
                print("1.- Lista de Keywords")
                print("2.- Lista de Softwords")
                userInput = input("Seleccione la lista que quiera ver... ")
                if userInput == "1":
                    print("Lista de Keywords: ")
                    # Imprime la lista de keywords
                    print(keyword.kwlist)
                    loop = False
                elif userInput == "2":
                    print("List de Softwords: ")
                    # Imprime la lista de softwords
                    print(keyword.softkwlist)
                    loop = False
                elif userInput == "3":
                    break
                else:
                    print("El valor ingresado es invalido.")
            elif menuSelection == "3":
                break
            else:
                print("El valor ingresado no es valido, intentelo denuevo.")
    elif menuSelection == "2":
        while loop:
            print("1.- Ver fecha de hoy")
            print("2.- Ver la hora actual")
            print("3.- Representar parametros como una fecha")
            print("4.- Combinar parametros para formar una fecha")
            print("5.- Formar una fecha y luego reemplazar un valor")
            print("6.- Volver")
            menuSelection = input("Ingrese el numero del programa que quiera ingresar...")
            if menuSelection == "1":
                # Se obtiene la fecha actual
                currentDate = date.today()
                # Se ordena la fecha
                formatedDateTwo = currentDate.strftime("%d/%b/%Y")
                print("La fecha actual es:",formatedDateTwo)
                loop = False
            elif menuSelection == "2":
                # Se obtiene la fecha y hora actual
                current = datetime.now()
                # Se ordena el tiempo a (Horas, minutos y segundos)
                currentTime = current.strftime("%H:%M:%S")
                print("La hora actual es:",currentTime)
                loop = False
            elif menuSelection == "3":
                # Se le pide al usuario ingresar el valor de dia, mes, año...
                day = int(input("Ingrese un numero de un dia: "))
                month = int(input("Ingrese un numero de un mes: "))
                year = int(input("Ingrese un año: "))
                hours = int(input("Ingrese horas: "))
                minutes = int(input("Ingrese minutos: "))
                sec = int(input("Ingrese segundos: "))
                # Se guarda esta variable que representa los valores integrados como fecha
                date = datetime(year, month, day, hours, minutes, sec).ctime()
                print("La fecha es: ",date)
                loop = False
            elif menuSelection == "4":
                # Se le pide al usuario ingresar el valor de dia, mes, año...
                day = int(input("Ingrese un numero de un dia: "))
                month = int(input("Ingrese un numero de un mes: "))
                year = int(input("Ingrese un año: "))
                hours = int(input("Ingrese horas: "))
                minutes = int(input("Ingrese minutos: "))
                date = date(year, month, day)
                time = time(hours, minutes)
                # Se combinan los valores de fecha y tiempo y se convierten en un objeto
                timeCombined = datetime.combine(date, time)
                print("La fecha es: ",timeCombined)
                loop = False
            elif menuSelection == "5":
                # Se le pide al usuario ingresar el valor de dia, mes y año
                day = int(input("Ingrese un numero de un dia: "))
                month = int(input("Ingrese un numero de un mes: "))
                year = int(input("Ingrese un año: "))
                date = date(year, month, day)
                print("La fecha ingresada es: ",date)
                print("1.- Cambiar dia")
                print("2.- Cambiar mes")
                print("3.- Cambiar año")
                value = input("Ingrese el valor que quiera reemplazar: ")
                if value == "1":
                    # Se reemplaza el dia con el valor ingresado
                    dateReplace = date.replace(day=15)
                    print("La nueva fecha es:",dateReplace)
                    loop = False
                elif value == "2":
                    # Se reemplaza el mes con el valor ingresado
                    dateReplace = date.replace(month=3)
                    print("La nueva fecha es:",dateReplace)
                    loop = False
                elif value == "3":
                    # Se reemplaza el año con el valor ingresado
                    dateReplace = date.replace(year=2077)
                    print("La fecha nueva es:",dateReplace)
                    loop = False
                else:
                    print("El valor ingresado es invalido")
                    loop = False
            elif menuSelection == "6":
                break
            else:
                print("El valor ingresado no es valido, intentelo denuevo.")
    else:
        print("El valor ingresado no es valido")
        break

'''
Integrantes del grupo:
- Isaac Huaman​
- Dick Sihuas
- Jesús Ramirez
- Fernando Vargas
'''