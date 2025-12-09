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

################################            VARIABLES GLOBALES
##### CONSTANTES Y VARIABLES
TARGET_WORD_SIZE = 5  # Constante de la longitud de la palabra
game_over = False # Variable de control del juego


################################            FUNCIONES

#####       1. Iniciar Juego

def get_random_word() -> list[str]:
    """
    Selecciona una palabra aleatoria de la lista de palabras posibles y la devuelve como lista de caracteres.
    
    Returns:
        list[str]: Lista de caracteres que representan la palabra aleatoria.
    """
    possible_words = ['P A N D A', 'J A M O N', 'A E R E O']

    random_index = randint(0, len(possible_words) - 1) # Índice aleatorio entre 0 y la longitud de la lista -1

    random_word = possible_words[random_index].split() # Divide la cadena en una lista de caracteres

    return random_word #Devuelve una lista de caracteres

def is_valid_word_characters(word: list) -> bool:
    """
    Verifica si todos los caracteres de la palabra son letras válidas (A-Z o Ñ).
    
    Args:
        word (list): Lista de caracteres a validar.
    
    Returns:
        bool: True si todos los caracteres son válidos, False en caso contrario.
    """
    is_valid = True
    for letter in word:
        if not ('A' <= letter <= 'Z' or letter == 'Ñ'):
            is_valid = False
            break
    # Se podría resumir todo en una sola línea pero sería menos legible por lo que lo dejamos así
    return is_valid

def is_word_length_valid(word: str) -> bool:
    """
    Verifica si la longitud de la palabra coincide con el tamaño objetivo.
    
    Args:
        word (str): La palabra a validar.
    
    Returns:
        bool: True si la longitud es correcta, False en caso contrario.
    """
    # valida = True
    # if len(word) != TARGET_WORD_SIZE:
    #     valida = False
    # return valida
        
    # Toda la logica se puede resumir en una sola linea usando un condicional:
    return len(word) == TARGET_WORD_SIZE # esto devuelve True o False directamente
    

#####       2. Palabra del Usuario VS Palabra Aleatoria

def get_user_word_input() -> str:
    """
    Solicita al usuario que introduzca una palabra válida y la devuelve en mayúsculas.
    
    Returns:
        str: La palabra introducida por el usuario en mayúsculas.
    """
    while True:
        user_word = input('Introduzca una palabra que contenga {} letras: '
                                .format(TARGET_WORD_SIZE)).upper()
        if not is_word_length_valid(user_word):
            print('\nLa palabra debe contener {} letras'.format(TARGET_WORD_SIZE))
            continue
        if not is_valid_word_characters(user_word):
            print('\nAlgún caracter no es válido en _{}_'.format(user_word))
            continue
        break
    return user_word

def match_positions(random_word_copy: list, new_word: list, result_list: list) -> tuple:
    """
    Compara las posiciones de las letras entre la palabra aleatoria y la palabra del usuario,
    marcando las letras correctas en la posición correcta en mayúsculas.
    
    Args:
        random_word_copy (list): Copia de la palabra aleatoria.
        new_word (list): La palabra introducida por el usuario.
        result_list (list): Lista de resultados parciales.
    
    Returns:
        tuple: Tupla con la copia modificada de la palabra aleatoria y la lista de resultados.
    """
    for position in range(len(new_word)):
        letter = new_word[position]
        
        if letter in random_word_copy:
            if random_word_copy[position] == letter:
                result_list[position] = letter.upper()
                random_word_copy[position] = None
                
    return random_word_copy, result_list

def match_letters(random_word_copy: list, new_word: list, result_list: list) -> list:
    """
    Compara las letras entre la palabra aleatoria y la palabra del usuario,
    marcando las letras correctas pero en posición incorrecta en minúsculas.
    
    Args:
        random_word_copy (list): Copia de la palabra aleatoria.
        new_word (list): La palabra introducida por el usuario.
        result_list (list): Lista de resultados parciales.
    
    Returns:
        list: Lista de resultados actualizada.
    """
    for position in range(len(new_word)):
        letter = new_word[position]
        
        if result_list[position] == ' ':
            if letter in random_word_copy and letter is not None:
                result_list[position] = letter.lower()
                random_word_copy[random_word_copy.index(letter)] = None
    return result_list

def check_word_match(random_word, new_word):
    """
    Compara la palabra aleatoria con la palabra del usuario y genera una lista de resultados
    indicando letras correctas en posición (mayúsculas), correctas pero mal posicionadas (minúsculas)
    o incorrectas (espacios).
    
    Args:
        random_word: La palabra aleatoria.
        new_word: La palabra introducida por el usuario.
    
    Returns:
        list: Lista de resultados con las letras marcadas.
    """
    result_list = [' '] * len(random_word) # [' ', ' ', ' ', ' ', ' ']
    random_word_copy = list(random_word)
    
    random_word_copy, result_list = match_positions(
        random_word_copy, new_word, result_list
    )
    result_list = match_letters(
        random_word_copy, new_word, result_list
    )
    
    return result_list

################################            FUNCIÓN GENERAL

def play_wordle():
    """
    Función principal que ejecuta el juego de Wordle.
    Selecciona una palabra aleatoria y permite al usuario adivinarla en turnos.
    """
    # ^ Este tipo de comentario se usa para documentar funciones en Python por lo que si pones el cursor encima de la función te aparecerá esta descripción.
    selected_word = get_random_word()

    ###### TURNOS
    while not game_over:
        entered_word = get_user_word_input()

        match_results = check_word_match(selected_word, entered_word)
        print('Palabra: ', '_'.join(match_results))

        if not is_valid_word_characters(match_results):
            continue # Si la palabra no es válida, volvemos al inicio del bucle
        
        print() #Visual
        print('ENHORABUENA, HAS GANADO')
        game_over = True # Cambiamos el estado de la variable de control
    

################################            JUGAR

# Declaramos el punto de entrada del programa: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    play_wordle()