import math


def movimiento_respecto_al_mouse(velocidad: float, posicion_jugador: tuple, posicion_mouse: tuple) -> tuple:

    zona_muerta = 10 # Un área alrededor del jugador donde no se genera movimiento

    # Se calcula el vector que se forma entre el jugador y el mouse
    vector_original = (
        posicion_mouse[0] - posicion_jugador[0],
        posicion_mouse[1] - posicion_jugador[1]
    )

    # La distancia entre los puntos genera la magnitud del vector
    magnitud = math.sqrt(vector_original[0] ** 2 + vector_original[1] ** 2)

    # En caso de que la magnitud sea
    if magnitud < zona_muerta:
        return 0, 0 # No se genera movimiento

    # Normalización del vector
    vector_unitario = (vector_original[0] / magnitud, vector_original[1] / magnitud)
    movimiento_x = vector_unitario[0] * velocidad
    movimiento_y = vector_unitario[1] * velocidad

    return movimiento_x, movimiento_y