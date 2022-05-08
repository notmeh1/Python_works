from datetime import date, datetime, time

print("1.- Ver fecha con formato norteamericano")
print("2.- Ver fecha con formato sudamericano")
print("3.- Ver Hora actual")
print("4.- Ver fecha y hora actual")

# Obtiene la fecha actual
currentDate = date.today()

# Obtiene la fecha y hora actual
current = datetime.now()

loop = True
while loop:
    userInput = input("Seleccione la lista que quiera ver... ")
    if userInput == "1":

        # Se ordena la fecha al formato regional Norteamericano
        formatedDateOne = currentDate.strftime("%B/%d/%Y")
        print("La fecha actual es:",formatedDateOne)

    elif userInput == "2":
        # Se ordena la fecha al formato regional Sudamericano
        formatedDateTwo = currentDate.strftime("%d/%b/%Y")

        print("La fecha actual es:",formatedDateTwo)
    elif userInput == "3":
        # Se obtiene la fecha y hora actual

        # Se ordena el tiempo a (Horas, minutos y segundos)
        currentTime = current.strftime("%H:%M:%S")
        print("La hora actual es:",currentTime)

    elif userInput == "4":
        # Se ordena el tiempo a (Dias, meses, años, horas, minutos y segundos)
        currentTimeComplete = current.strftime("%d/%b/%Y"+" " +"%H:%M:%S")
        print("La fecha y hora actual es: ",currentTimeComplete)
    else:
        print("El valor ingresado es invalido.")