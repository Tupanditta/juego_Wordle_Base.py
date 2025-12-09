# Wordle - Lógica y Estructura

Este proyecto se basa en el típico juego del **Wordle**, juego el cual tiene como objetivo principal hayar la palabra secreta.
Para ello, el jugador introduce una palabra, y el programa compara dicha palabra con la palabra secreta, finalmente devolviendo dicha comparativa de modo que el jugador obtiene va obteniendo pistas. 

## Arquitectura del Código

El programa está dividido en diferentes funciones, las cuales se aplican en la función general del juego (`Wordle`).
Dichas funciones tienen como fin general...

      --> Crear (inicializar) la partida, elijiendo la palabra secreta.
      --> Pedir al usuario una palabra con las mismas dimensiones que la palabra secreta.
      --> Comparar la palabra introducida por el usuario y la palabra secreta.
      --> Mostrar el resultado; diciendo que letras están colocadas en su posición, 
          cuales no se hayan en su posición y cuales no forman parte de la palabra secreta.

### Flujo del Código



### Optimización del Código

Actualmente el archivo "JUEGO_Wordle_Base" contiene el código del juego base. Es por ello que existen diferentes mejoras que se pueden implementar en el código para hacerlo más visual y entretenido (las dejo como puntos de mejora para versiones posteriores).
