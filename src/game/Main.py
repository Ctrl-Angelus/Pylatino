import pygame
from pygame.rect import Rect

from Entidades import Jugador
from Parametros import *


DIMENSIONES_DEL_LIENZO = list()


def main():
    pygame.init()

    informacion = pygame.display.Info()
    alto = informacion.current_h * 0.9
    ancho = alto
    DIMENSIONES_DEL_LIENZO.append(ancho)
    DIMENSIONES_DEL_LIENZO.append(alto)

    pygame.display.set_caption(TITULO)

    escena = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
    tiempo = pygame.time.Clock()

    jugador = Jugador(Rect(0, 0, TAMAÑO, TAMAÑO), VELOCIDAD)

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        teclas = pygame.key.get_pressed()
        jugador.mover(teclas, DIMENSIONES_DEL_LIENZO)

        escena.fill((0, 0, 0))
        pygame.draw.rect(escena, (0, 0, 255), jugador.cuerpo, 0, 100)
        pygame.display.update()
        tiempo.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
