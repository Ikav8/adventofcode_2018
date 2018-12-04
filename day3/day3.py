""""
#1 @ 53,238: 26x24
El cuadrado con ID 1 está situado a
    53 puntos del limite izquierdo.
    238 puntos del limite superior.
Y mide
    26 puntos de ancho.
    24 puntos de largo.
"""

# Part 1 #

fabrica = [[0]*1000 for i in range(1000)]

with open(file='day3_input.txt') as input:

    coordenadas_list = input.read().splitlines()
    # coordenada_list = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

    for coordenada in coordenadas_list:

        coordenada_split = coordenada.split(' ')

        id = coordenada_split[0]
        limite_izda = coordenada_split[2].split(',')[0]
        limite_sup = coordenada_split[2].split(',')[1][0:-1]
        ancho = coordenada_split[3].split('x')[0]
        alto = coordenada_split[3].split('x')[1]

        for y in range(0, int(alto)):
            for x in range(0, int(ancho)):

                x_total = int(limite_izda) + x
                y_total = int(limite_sup) + y
                if fabrica[x_total][y_total] == 0:
                    fabrica[x_total][y_total] = id
                else:
                    fabrica[x_total][y_total] = 'X'

    number_of_X = 0
    for fab in fabrica:
        number_of_X += fab.count('X')
    print('Parte 1: ' + str(number_of_X))

    for fab in fabrica:
        print(fab)

# Parte 2 #

    for coordenada in coordenadas_list:

        coordenada_split = coordenada.split(' ')

        id = coordenada_split[0]
        limite_izda = coordenada_split[2].split(',')[0]
        limite_sup = coordenada_split[2].split(',')[1][0:-1]
        ancho = coordenada_split[3].split('x')[0]
        alto = coordenada_split[3].split('x')[1]

        numero_de_X = 0

        for y in range(0, int(alto)):
            for x in range(0, int(ancho)):

                x_total = int(limite_izda) + x
                y_total = int(limite_sup) + y
                if fabrica[x_total][y_total] == 'X':
                    numero_de_X += 1
                    break


        if numero_de_X == 0:
            print('Parte 2: ' + id)