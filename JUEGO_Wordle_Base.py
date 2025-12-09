####################################################

# Autor: Ander Lifeng Sola
# Alias: Tupanditta :)
# Color Favorito: Azul Stich

# Fecha: Ma 09/12/2025
# Archivo: JUEGO_Wordle_Base.py
# Descripción: Juego del wordle.

####################################################

################################            LIBRERÍAS

from random import randint


################################            FUNCIONES

#####       1. Iniciar Juego

def escoger_palabra_aleatoria(): 
    lista_palabras_posibles = ['P A N D A', 'J A M O N', 'A E R E O']

    num_aleatorio = randint(0, len(lista_palabras_posibles) - 1)

    palabra_aleatoria = lista_palabras_posibles[num_aleatorio].split()

    return palabra_aleatoria #Devuelve una lista de caracteres

def preguntar_palabra_usuario(N): 
    palabra_usuario = input('Introduzca una palabra que contenga {} letras: '.format(N))
    palabra_usuario = palabra_usuario.upper()

    return palabra_usuario

def palabra_valida_caracteres(palabra): 
    valida = True
    for letra in palabra:
        if not ('A' <= letra <= 'Z' or letra == 'Ñ'):
            valida = False
            break

    return valida

def palabra_valida_longitud(palabra, N): 
    valida = True
    if len(palabra) != N:
        valida = False
    
    return valida

#####       2. Palabra del Usuario VS Palabra Aleatoria

def añadir_nueva_palabra(N): 
    while True:
        palabra_usuario = preguntar_palabra_usuario(N)
        if palabra_valida_caracteres(palabra_usuario) and palabra_valida_longitud(palabra_usuario, N):
            break
        
        if not palabra_valida_longitud(palabra_usuario, N):
            print() #Visual
            print('La palabra debe contener {} letras'.format(N))

        if not palabra_valida_caracteres(palabra_usuario):
            print() #Visual
            print('Algún caracter no es válido en _{}_'.format(palabra_usuario))
    
    return palabra_usuario

def coinciden_posiciones(palabra_aleatoria_espejo, nueva_palabra, lista_resultado):
    for posicion in range(len(nueva_palabra)):
        letra = nueva_palabra[posicion]

        if letra in palabra_aleatoria_espejo:
            if palabra_aleatoria_espejo[posicion] == letra:
                lista_resultado[posicion] = letra.upper()
                palabra_aleatoria_espejo[posicion] = None
    
    return palabra_aleatoria_espejo, lista_resultado

def conciden_letras(palabra_aleatoria_espejo, nueva_palabra, lista_resultado):
    for posicion in range(len(nueva_palabra)):
        letra = nueva_palabra[posicion]

        if lista_resultado[posicion] == ' ':
            if letra in palabra_aleatoria_espejo and letra is not None:
                lista_resultado[posicion] = letra.lower()
                palabra_aleatoria_espejo.remove(letra)

    return lista_resultado

def letra_correcta(palabra_aleatoria_espejo, nueva_palabra, lista_resultado):
    palabra_aleatoria_espejo, lista_resultado = coinciden_posiciones(palabra_aleatoria_espejo, nueva_palabra, lista_resultado)
    
    lista_resultado = conciden_letras(palabra_aleatoria_espejo, nueva_palabra, lista_resultado)
    
    return lista_resultado

def comparar_palabras(palabra_aleatoria, nueva_palabra):
    lista_resultado = [' ', ' ', ' ', ' ', ' ']

    palabra_aleatoria_espejo = list(palabra_aleatoria)

    lista_resultado = letra_correcta(palabra_aleatoria_espejo, nueva_palabra, lista_resultado)
    
    return lista_resultado

def mostrar_respuesta(palabra_aleatoria, nueva_palabra):
    lista_resultado = comparar_palabras(palabra_aleatoria, nueva_palabra)
    
    print(lista_resultado)

    return lista_resultado

def comprobar_terminado(lista_resultado):
    terminado = True

    for letra in lista_resultado:
        if not ('A' <= letra <= 'Z' or letra == 'Ñ'):
            terminado = False
            break
    
    return terminado


################################            FUNCIÓN GENERAL

def wordle():
    ###### INICIO
    N = 5 #Constante de la longitud
    terminado = False

    palabra_aleatoria = escoger_palabra_aleatoria()

    ###### TURNOS
    while not terminado:
        nueva_palabra = añadir_nueva_palabra(N)

        lista_resultado = mostrar_respuesta(palabra_aleatoria, nueva_palabra)

        if comprobar_terminado(lista_resultado):
            print() #Visual
            print('ENHORABUENA, HAS GANADO')

            break
    

################################            JUGAR

wordle()


