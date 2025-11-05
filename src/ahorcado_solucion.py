"""
Juego del Ahorcado - SOLUCIÓN PROPUESTA
========================================

Esta es una posible solución al ejercicio del ahorcado.
Se proporciona como referencia para discusión en clase.

NOTA PARA EL PROFESOR: Este archivo contiene una implementación completa
que puede usar como base para la discusión con los alumnos.

Autor: revilofe
"""


def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)


def solicitar_palabra():
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns:
        str: La palabra a adivinar en mayúsculas
    """
    while True:
        palabra = input("Jugador 1: Introduce la palabra a adivinar (mínimo 5 letras): \n> ")
        
        # Verificar que tenga al menos 5 caracteres
        if len(palabra) < 5:
            print("Error: La palabra debe tener al menos 5 caracteres.\n")
            continue
        
        # Verificar que solo contenga letras
        if not palabra.isalpha():
            print("Error: La palabra solo puede contener letras.\n")
            continue
        
        # Si llegamos aquí, la palabra es válida
        return palabra.upper()


def solicitar_letra(letras_usadas):
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Args:
        letras_usadas (list): Lista de letras ya introducidas
        
    Returns:
        str: La letra introducida en mayúsculas
    """
    while True:
        letra = input("\nIntroduce una letra: ")
        
        # Verificar que sea solo un carácter
        if len(letra) != 1:
            print("Error: Debes introducir solo una letra.")
            continue
        
        # Verificar que sea una letra
        if not letra.isalpha():
            print("Error: Debes introducir una letra (no números ni símbolos).")
            continue
        
        letra = letra.upper()
        
        # Verificar que no esté ya usada
        if letra in letras_usadas:
            print(f"Error: Ya has usado la letra '{letra}'. Prueba con otra.")
            continue
        
        # Si llegamos aquí, la letra es válida
        return letra


def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego
    
    Args:
        palabra_oculta (str): La palabra con _ y letras adivinadas
        intentos (int): Número de intentos restantes
        letras_usadas (list): Lista de letras ya usadas
    """
    print("\n" + "=" * 40)
    print(f"Intentos restantes: {intentos}")
    
    # Mostrar la palabra con espacios entre caracteres
    palabra_con_espacios = " ".join(palabra_oculta)
    print(f"Palabra: {palabra_con_espacios}")
    
    print(f"Letras usadas: {letras_usadas}")
    print("=" * 40)


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Args:
        palabra (str): La palabra completa a adivinar
        palabra_oculta (str): La palabra actual con _ y letras adivinadas
        letra (str): La letra que se ha adivinado
        
    Returns:
        str: La palabra oculta actualizada
    """
    # Convertir palabra_oculta a lista para poder modificarla
    lista_palabra_oculta = list(palabra_oculta)
    
    # Recorrer la palabra y actualizar las posiciones donde aparece la letra
    for i, caracter in enumerate(palabra):
        if caracter == letra:
            lista_palabra_oculta[i] = letra
    
    # Convertir la lista de vuelta a string
    return "".join(lista_palabra_oculta)


def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    INTENTOS_MAXIMOS = 5
    
    # Solicitar la palabra al jugador 1
    palabra = solicitar_palabra()
    
    # Limpiar la pantalla para que el jugador 2 no vea la palabra
    limpiar_pantalla()
    
    # Inicializar variables del juego
    palabra_oculta = "_" * len(palabra)  # Crear string con _ del mismo tamaño que la palabra
    intentos = INTENTOS_MAXIMOS
    letras_usadas = []
    ganado = False
    
    print("Jugador 2: ¡Adivina la palabra!\n")
    
    # Bucle principal del juego
    while intentos > 0 and not ganado:
        # Mostrar el estado actual
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
        
        # Solicitar una letra
        letra = solicitar_letra(letras_usadas)
        
        # Añadir la letra a las letras usadas
        letras_usadas.append(letra)
        
        # Verificar si la letra está en la palabra
        if letra in palabra:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            
            # Actualizar palabra_oculta
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            
            # Comprobar si se ha ganado (ya no hay '_' en palabra_oculta)
            if "_" not in palabra_oculta:
                ganado = True
        else:
            print(f"¡Letra incorrecta! La letra '{letra}' no está en la palabra.")
            intentos -= 1
    
    # Mostrar mensaje final
    print("\n" + "=" * 40)
    if ganado:
        print("¡FELICIDADES! Has adivinado la palabra: " + palabra)
    else:
        print("¡GAME OVER! Te has quedado sin intentos.")
        print(f"La palabra era: {palabra}")
    print("=" * 40 + "\n")


def main():
    """
    Punto de entrada del programa
    """
    jugar()
    
    # Preguntar si quiere jugar otra vez
    jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() == 's':
        print("\n")
        main()
    else:
        print("¡Gracias por jugar!")


if __name__ == "__main__":
    main()
