print("=== Bienvenido al Juego de Trivia ===")
print("Responde correctamente a las preguntas. Tienes 3 vidas.\n")

vidas = 3
puntaje = 0

preguntas = {
    "¿Cuál es la capital de Francia?": "Paris",
    "¿Cuánto es 5 * 6?": 35,   
    "¿Cuál es el color del cielo de día?": "azul"
}

for pregunta, respuesta_correcta in preguntas.items():
    print(pregunta)
    respuesta_usuario = input("Tu respuesta: ")

    if respuesta_usuario.lower() == respuesta_correcta:  
        print("¡Correcto!\n")
        puntaje = puntaje + 1
    else:
        print("Incorrecto. La respuesta era:", respuesta_correcta, "\n")
        vidas = vidas - 1

    if vidas <= 0:
        print("😢 Te quedaste sin vidas.")
        break

print("Juego terminado.")
print("Tu puntaje fue:", puntos)  
