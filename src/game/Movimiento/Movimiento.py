import math
from typing import Optional


def movimiento_relativo(velocidad: float, posicion_actual: tuple, posicion_objetivo: tuple, rango: Optional[float]) -> tuple:

    zona_muerta: float = 10 # Una zona (en píxeles) alrededor del objetivo que previene magnitudes (distancias entre puntos) de cero

    # Se calcula el vector que se forma entre el jugador y el mouse
    vector_original = (
        posicion_objetivo[0] - posicion_actual[0],
        posicion_objetivo[1] - posicion_actual[1]
    )

    # La distancia entre los puntos genera la magnitud del vector
    magnitud = math.sqrt(vector_original[0] ** 2 + vector_original[1] ** 2)

    if rango is not None:
        if magnitud > rango:
            return 0, 0

    # En caso de que la magnitud sea menor a la zona muerta no se genera movimiento
    if magnitud < zona_muerta:
        return 0, 0

    # Normalización del vector
    vector_unitario = (vector_original[0] / magnitud, vector_original[1] / magnitud)
    movimiento_x = vector_unitario[0] * velocidad
    movimiento_y = vector_unitario[1] * velocidad

    return movimiento_x, movimiento_y

