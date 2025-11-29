from pygame import Rect


def desplazamiento_y_colision(personaje: Rect, desplazamiento: tuple, fondo: Rect, direccion: int) -> tuple:

    simulacion: Rect = fondo.move(
        desplazamiento[0] * direccion,
        desplazamiento[1] * direccion
    )

    # Se verifica si la versión simulada del fondo choca o sobrepasa las coordenadas del personaje
    colision_izquierda: bool = simulacion.left >= personaje.left
    colision_derecha: bool = simulacion.right <= personaje.right

    colision_arriba: bool = simulacion.top >= personaje.top
    colision_abajo: bool = simulacion.bottom <= personaje.bottom

    # El movimiento por defecto lo da el desplazamiento original, se modifica en caso de ser necesario
    movimiento_x: float = desplazamiento[0] * direccion
    movimiento_y: float = desplazamiento[1] * direccion

    # En caso de haber colisiones, se modifica el movimiento lo justo para que el personaje alcance el borde sin pasarlo
    if colision_izquierda:
        movimiento_x = personaje.left - fondo.left

    elif colision_derecha:
        movimiento_x = personaje.right - fondo.right

    if colision_arriba:
        movimiento_y = personaje.top - fondo.top

    elif colision_abajo:
        movimiento_y = personaje.bottom - fondo.bottom

    return movimiento_x, movimiento_y

def desplazamiento_y_colision_enemigos(personaje: Rect, desplazamiento: tuple, fondo: Rect, direccion: int) -> tuple:

    simulacion: Rect = personaje.move(
        desplazamiento[0] * direccion,
        desplazamiento[1] * direccion
    )

    # Se verifica si la versión simulada del fondo choca o sobrepasa las coordenadas del personaje
    colision_izquierda: bool = simulacion.left <= fondo.left
    colision_derecha: bool = simulacion.right >= fondo.right

    colision_arriba: bool = simulacion.top <= fondo.top
    colision_abajo: bool = simulacion.bottom >= fondo.bottom

    # El movimiento por defecto lo da el desplazamiento original, se modifica en caso de ser necesario
    movimiento_x: float = desplazamiento[0] * direccion
    movimiento_y: float = desplazamiento[1] * direccion

    # En caso de haber colisiones, se modifica el movimiento lo justo para que el personaje alcance el borde sin pasarlo
    if colision_izquierda:
        movimiento_x += fondo.left - simulacion.left

    elif colision_derecha:
        movimiento_x += fondo.right - simulacion.right

    if colision_arriba:
        movimiento_y += fondo.top - simulacion.top

    elif colision_abajo:
        movimiento_y += fondo.bottom - simulacion.bottom

    return movimiento_x, movimiento_y