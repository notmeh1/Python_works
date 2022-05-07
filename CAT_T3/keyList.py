import keyword

print("1.- Lista de Keywords")
print("2.- Lista de Softwords")
userInput = input("Seleccione la lista que quiera ver... ")
if userInput == "1":
    print("Lista de Keywords: ")
    # Imprime la lista de keywords
    print(keyword.kwlist)
elif userInput == "2":
    print("List de Softwords: ")
    # Imprime la lista de softwords
    print(keyword.softkwlist)
else:
    print("El valor ingresado es invalido.")