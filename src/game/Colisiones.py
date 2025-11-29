
from pygame import Rect

def colision_con_el_limite(personaje: Rect, fondo_con_desplazamiento: Rect) -> dict:

    # Se verifica si la versión simulada del fondo choca o sobrepasa las coordenadas del personaje
    colision_izquierda: bool = fondo_con_desplazamiento.left >= personaje.left
    colision_derecha: bool = fondo_con_desplazamiento.right <= personaje.right

    colision_arriba: bool = fondo_con_desplazamiento.top >= personaje.top
    colision_abajo: bool = fondo_con_desplazamiento.bottom <= personaje.bottom

    return {
        "derecha" : colision_derecha,
        "izquierda" : colision_izquierda,
        "arriba" : colision_arriba,
        "abajo" : colision_abajo,
    }