import math


def movimiento_relativo(velocidad: float, posicion_actual: tuple, posicion_objetivo: tuple, zona_muerta: float, distancia) -> tuple:

    # Se calcula el vector que se forma entre el jugador y el mouse
    vector_original = (
        posicion_objetivo[0] - posicion_actual[0],
        posicion_objetivo[1] - posicion_actual[1]
    )

    # La distancia entre los puntos genera la magnitud del vector
    if distancia is None:
        magnitud = math.sqrt(vector_original[0] ** 2 + vector_original[1] ** 2)
    else:
        magnitud = distancia

    # En caso de que la magnitud sea
    if magnitud < zona_muerta:
        return 0, 0 # No se genera movimiento

    # Normalización del vector
    vector_unitario = (vector_original[0] / magnitud, vector_original[1] / magnitud)
    movimiento_x = vector_unitario[0] * velocidad
    movimiento_y = vector_unitario[1] * velocidad

    return movimiento_x, movimiento_y