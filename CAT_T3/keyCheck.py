import keyword

inputList = []
loop = True
while loop:
    print('--------------------------------' * 2)
    userInput = input("Escriba algo... ")

    # Retorna un boolean si el string indicado contiene alguna keyword
    keyCheck = 'Si' if keyword.iskeyword(userInput) else 'No'
    # Retorna un boolean si el string indicado contiene alguna softword
    softCheck = 'Si' if keyword.issoftkeyword(userInput) else 'No'
    item = {
        'Entrada del usuario': userInput,
        'Contiene alguna keyword?': keyCheck,
        'Contiene alguna softword?': softCheck
    }
    inputList.append(item)
    for item in inputList:
        print(item)
