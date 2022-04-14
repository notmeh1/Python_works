# Seudocodigo aqui

#--------------------------------------------------

# Solicitar Nombre y apellido al usuario.

fullName = input("Escriba su nombre y apellido: ")
# Solicitar el número de productos que compró el usuario.
productQty = int(input("¿Cuantos productos llevó durante su ultima compra? : "))
# Solicitar el monto de dinero que el usuario pago.
totalPrice = int(input("¿Cuánto pago por el total de su compra? : "))

if productQty < 10 and totalPrice <= 10000:
    print("Lo sentimos, usted no aplica para un descuento.")
elif productQty > 10 and totalPrice > 10000 and totalPrice < 30000:
    print("Descuento de 8.5%")
elif productQty > 15 and totalPrice > 30000 and totalPrice < 45000:
    print("Descuento de 12.65%")
elif productQty > 15 and productQty < 30 and totalPrice > 45000 and totalPrice < 72000:
    print("Descuento de 15.75%")
elif productQty > 20 and productQty < 40 and totalPrice > 72000 and totalPrice < 96000:
    print("Descuento de 20.5%")
elif productQty > 20 and productQty < 40 and totalPrice > 96000:
    print("Descuento de 25.67%")
