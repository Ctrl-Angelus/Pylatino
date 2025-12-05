from math import atan2, degrees


def calcular_angulo(posicion_1: tuple, posicion_2: tuple) -> float:
    x1 = posicion_1[0]
    y1 = posicion_1[1]

    x2 = posicion_2[0]
    y2 = posicion_2[1]

    angulo = atan2(y2 - y1, x2 - x1)

    angulo_grados = degrees(angulo)

    return angulo_grados