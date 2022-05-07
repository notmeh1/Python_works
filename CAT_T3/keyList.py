import keyword

print("1.- Lista de Keywords")
print("2.- Lista de Softwords")
userInput = input("Seleccione la lista que quiera ver... ")
if userInput == "1":
    print("Lista de Keywords: ")
    print(keyword.kwlist)
elif userInput == "2":
    print("List de Softwords: ")
    print(keyword.softkwlist)
else:
    print("El valor ingresado es invalido.")