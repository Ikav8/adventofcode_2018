import string

with open('day5_input.txt') as input:

    polymer = input.read()

    tipos = []
    for minuscula, mayuscula in zip(string.ascii_lowercase, string.ascii_uppercase):
        tipos.append(minuscula+mayuscula)
        tipos.append(mayuscula+minuscula)



    while 1:

        len_antes = len(polymer)
        for tipo in tipos:
            polymer = polymer.replace(tipo, '')

        if len(polymer) == len_antes:
            break
    print(polymer)
    print(len(polymer))

    # parte 2 #

    print('Parte 2')


with open('day5_input.txt') as input:

    best_solution = 9999999

    polymer_original = input.read()
    for minuscula, mayuscula in zip(string.ascii_lowercase, string.ascii_uppercase):
        polymer = polymer_original
        polymer = polymer.replace(minuscula, '')
        polymer = polymer.replace(mayuscula, '')
        print(polymer)
        print('Empieza ' + mayuscula)
        while 1:
            salir = False
            len_antes = len(polymer)
            for tipo in tipos:
                polymer = polymer.replace(tipo, '')

            len_despues = len(polymer)

            #print(mayuscula + ' antes: ' + str(len_antes) + ' despues: ' + str(len_despues))
            if len_despues == len_antes:
                print(mayuscula + ' - ' + str(len_despues))
                break
    print(best_solution)