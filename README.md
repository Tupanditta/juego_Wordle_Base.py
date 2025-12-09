# Wordle - Lógica y Estructura

Este proyecto se basa en el típico juego del **Wordle**, juego el cual tiene como objetivo principal hayar la palabra secreta.
Para ello, el jugador introduce una palabra, y el programa compara dicha palabra con la palabra secreta, finalmente devolviendo dicha comparativa 
de modo que el jugador va obteniendo pistas conforme introduce nuevas palabras.

## Arquitectura del Código

El programa está dividido en diferentes funciones, las cuales se aplican en la función general del juego (`Wordle`).
Dichas funciones tienen como fin general...

      --> Crear (inicializar) la partida, elijiendo la palabra secreta.
      --> Pedir al usuario una palabra con las mismas dimensiones que la palabra secreta.
      --> Comparar la palabra introducida por el usuario y la palabra secreta.
      --> Mostrar el resultado; diciendo que letras están colocadas en su posición, 
          cuales no se hayan en su posición y cuales no forman parte de la palabra secreta.

### Flujo del Código

1. Inicio: El programa selecciona una palabra secreta aleatoria de una lista predefinida (ej. "PANDA").

2. Bucle de Juego (Turnos): Se inicia el ciclo principal que se repite indefinidamente hasta que el jugador gana.

    //// Entrada de Datos: Se solicita al usuario que introduzca una palabra nueva.
    
    //// Validación: Se comprueba si la palabra introducida cumple las reglas antes de jugar.

           --> Verificación de Requisitos: Se mira si la longitud es correcta (N letras) y si los caracteres son válidos (A-Ñ).

                 % % Si no es válida: Muestra un mensaje de error específico y vuelve a pedir la entrada.

                 % % Si es válida: La palabra es aceptada y pasa a la fase de comparación.

    //// Análisis de la Palabra (Lógica Wordle): Se compara la palabra del usuario con la secreta en dos fases estrictas.

           --> Fase 1 (Posiciones Exactas): Primero se buscan letras que coinciden perfectamente en lugar y tipo.

                 % % Acción: Se guardan como MAYÚSCULAS en el resultado y se eliminan de la copia de la palabra secreta.

           --> Fase 2 (Coincidencias Parciales): Después se buscan letras que existen en la palabra secreta pero están en otra posición.

                 % % Acción: Se verifica si esa letra sigue disponible en la copia secreta. Si está, se guarda como minúscula y se elimina de la copia.

    //// Visualización: Se imprime la lista de resultados (ej. ['P', ' ', 'N', 'a', ' ']) para dar pistas al jugador.

    //// Verificación de Victoria: Se analiza la lista de resultados final.

           --> Comprobación: ¿Son todas las letras Mayúsculas?

                 % % Si no lo son: El turno termina y el bucle vuelve a empezar (pide nueva palabra).

                 % % Si lo son: Se muestra el mensaje "ENHORABUENA, HAS GANADO" y se rompe el bucle (Fin del Programa).

### Optimización del Código

Actualmente el archivo "JUEGO_Wordle_Base" contiene el código del juego base. Es por ello que existen diferentes mejoras que se pueden implementar en el código 
para hacerlo más visual y entretenido (las dejo como puntos de mejora para versiones posteriores).

      --> Al la hora de proporcionar pistas, en vez de mostrar la letra en mayúscula, minúscula o un vacío, utilizar diferentes colores para los diferentes casos
      --> Añadir la mecánica de oportunidades; si el jugador introduce N palabras incorrectas, pierde (Establecer un límite de intentos).
      --> Actualmente se muestra una lista como resultado; se puede hacer más visual cambiando el diseño.
      
