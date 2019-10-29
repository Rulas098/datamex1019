import random
# 1 = si, 0 = no
continuar = 1
while continuar == 1:
    print('Bienvenido/a a Megamente')
    print('Elija la dificultad del juego < 1 = Easy, 2 = Medium, 3 = Hard')
    dificultad = int(input('Digite el numero de dificultad '))

    if dificultad == 1:
        cant_digitos = 1
    elif dificultad == 2:
        cant_digitos = 2
    elif dificultad == 3:
        cant_digitos = 3

    digitos = ('0','1','2','3','4','5','6','7','8','9')
    codigo = ''

    for i in range(cant_digitos):
        elegido = random.choice(digitos)
        while elegido in codigo:
            elegido = random.choice(digitos)
        codigo = codigo + elegido
    print (codigo)
    print('Tenes que adivinar un codigo de', cant_digitos, 'digitos distintos')
    propuesta = input(' Que codigo propones?: ')

    intentos = 1

    while propuesta != codigo:
        intentos = intentos + 1
        aciertos = 0
        coincidencias = 0
        for i in range(cant_digitos):
            if propuesta[i] == codigo[i]:
                aciertos = aciertos + 1
            elif propuesta[i] in codigo:
                coincidencias = coincidencias + 1
        print('Tu propuesta(', propuesta,') tiene ', aciertos,
              'acierto y ', coincidencias, ' coincidencias')
        propuesta = input('Escribe otro codigo ')
    print('FELICIDADES! adivinaste el codigo en', intentos, ' intentos')
    continuar = int(input('Desea seguir jugando?: 1 = Si, 0 = No, < '))