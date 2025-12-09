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

################################            FUNCIÓN GENERAL

def wordle():
    palabra_aleatoria = escoger_palabra_aleatoria()
    print(palabra_aleatoria) #PANDA: borrar

################################            JUGAR

wordle()


