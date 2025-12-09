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
    possible_words = ['P A N D A', 'J A M O N', 'A E R E O']

    random_index = randint(0, len(possible_words) - 1) # Índice aleatorio entre 0 y la longitud de la lista -1

    random_word = possible_words[random_index].split() # Divide la cadena en una lista de caracteres

    return random_word #Devuelve una lista de caracteres

def is_valid_word_characters(word: list) -> bool:
    is_valid = True
    for letter in word:
        if not ('A' <= letter <= 'Z' or letter == 'Ñ'):
            is_valid = False
            break
    # Se podría resumir todo en una sola línea pero sería menos legible por lo que lo dejamos así
    return is_valid

def is_word_length_valid(word: str) -> bool:
    # valida = True
    # if len(word) != TARGET_WORD_SIZE:
    #     valida = False
    # return valida
        
    # Toda la logica se puede resumir en una sola linea usando un condicional:
    return len(word) == TARGET_WORD_SIZE # esto devuelve True o False directamente
    

#####       2. Palabra del Usuario VS Palabra Aleatoria

def get_user_word_input() -> str:
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
    for position in range(len(new_word)):
        letter = new_word[position]
        
        if letter in random_word_copy:
            if random_word_copy[position] == letter:
                result_list[position] = letter.upper()
                random_word_copy[position] = None
                
    return random_word_copy, result_list

def match_letters(random_word_copy: list, new_word: list, result_list: list) -> list:
    for position in range(len(new_word)):
        letter = new_word[position]
        
        if result_list[position] == ' ':
            if letter in random_word_copy and letter is not None:
                result_list[position] = letter.lower()
                random_word_copy[random_word_copy.index(letter)] = None
    return result_list

def check_word_match(random_word, new_word):
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