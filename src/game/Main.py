import pygame

from Entidades import Jugador
from Parametros import *
from Imagen import Imagen


def main():
    pygame.init()

    pygame.display.set_caption(TITULO)

    escena = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
    tiempo = pygame.time.Clock()

    fondo = Imagen("src/recursos/fondo.png", 2)

    fondo_estatico = Imagen("src/recursos/fondo-estatico.png", 1)

    fondo.rect.x = -(fondo.width - DIMENSIONES_DEL_LIENZO[0]) / 2
    fondo.rect.y = -(fondo.height - DIMENSIONES_DEL_LIENZO[1]) / 2

    posicion_inicial_x = escena.get_rect().center[0] - MEDIDA_DE_TILE / 2
    posicion_inicial_y = escena.get_rect().center[1] - MEDIDA_DE_TILE / 2

    jugador = Jugador(posicion_inicial_x, posicion_inicial_y, MEDIDA_DE_TILE, MEDIDA_DE_TILE, VELOCIDAD)

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        teclas_presionadas = pygame.key.get_pressed()

        if teclas_presionadas[jugador.controles.get("adelante")]:
            posicion_mouse = pygame.mouse.get_pos()

            jugador.mover(posicion_mouse, fondo.rect)

        escena.blit(fondo_estatico.imagen, fondo_estatico.rect)
        escena.blit(fondo.imagen, fondo.rect)

        escena.blit(jugador.sprite, jugador.cuerpo)
        pygame.display.flip()
        tiempo.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
