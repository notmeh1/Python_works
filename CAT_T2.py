# Seudocodigo aqui
"""
Pasos a realizar:
1. Solicitar datos al usuario (Nombre completo, Cantidad de productos que compró y 
Total de la compra).
2. Dependiendo de los datos ingresados, asignar un porcentaje de descuento y calcular
el descuento en dinero. (En el caso de que los datos cumplan con los requisitos para obtener
el descuento).
3. Una vez calculado el descuento, retornar al usuario el descuento de dinero para su proxima
compra/Devolver al usuario un mensaje que le informe si obtuvo o no el descuento.
"""

#--------------------------------------------------
import time
print("Bienvenido al programa de recompensas de XYZ \nInserte los datos y tendra la posibilidad de ganar descuentos en su proxima compra.")
time.sleep(5)

# Solicitar Nombre y apellido al usuario.
fullName = input("Escriba su nombre y apellido: ")
# Solicitar el número de productos que compró el usuario.
productQty = input("¿Cuantos productos llevó durante su ultima compra? : ")
try:
    productQty = int(productQty)
    # Solicitar el monto de dinero que el usuario pago.
    totalPrice = input("¿Cuánto pago por el total de su compra? : ")
    try:
        totalPrice = int(totalPrice)

        # Funcion que calcula el descuento
        def calcDiscount(discount, totalPrice):
            finalDiscount = (discount * totalPrice) / 100
            finalDiscount = round(finalDiscount)
            #print("Felicidades usted ha ganado un descuento de $",finalDiscount,"en su proxima compra!")
            #print("Descuento de",discount,"%")
            print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
            print(f"{'Nombre del cliente: ' : <20}{'' : ^15}{fullName : >20}")
            print(f"{'Monto de la ultima compra: ' : <20}{'' : ^15}{totalPrice : >20}")
            print(f"{'Numero de productos adquiridos: ' : <20}{'' : ^15}{productQty : >20}")
            print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
            print("Usted acaba de ganar un cupon de descuento para su proxima compra por un \nmonto de $",finalDiscount,"equivalente al",discount,"% de su ultima compra.")
            print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")

        # Condiciones
        if productQty < 10 and totalPrice <= 10000:
            print("Lo sentimos, usted no aplica para un descuento.")
        elif productQty > 10 and totalPrice > 10000 and totalPrice <= 30000:
            discount = 8.5
            calcDiscount(discount, totalPrice)
        elif productQty > 15 and totalPrice > 30000 and totalPrice <= 45000:
            discount = 12.65
            calcDiscount(discount, totalPrice)
        elif productQty > 15 and productQty <= 30 and totalPrice > 45000 and totalPrice <= 72000:
            discount = 15.75
            calcDiscount(discount, totalPrice)
        elif productQty > 20 and productQty <= 40 and totalPrice > 72000 and totalPrice <= 96000:
            discount = 20.5
            calcDiscount(discount, totalPrice)
        elif productQty > 20 and productQty <= 40 and totalPrice > 96000:
            discount = 25.67
            calcDiscount(discount, totalPrice)
        else:
            print("Lo sentimos, usted no aplica para un descuento.")
    # Error en caso de que el usuario no inserte caracteres indicados.
    except ValueError:
        print("Los valores entregados se encuentran fuera del rango esperado")
# Error en caso de que el usuario no inserte caracteres indicados.
except ValueError:
    print("Los valores entregados se encuentran fuera del rango esperado")

