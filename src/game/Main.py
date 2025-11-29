import pygame
import random

from Entidades import Jugador, Entidad
from Parametros import *
from Sprite import Sprite


def main():
    pygame.init()

    pygame.display.set_caption(TITULO)

    escena = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
    tiempo = pygame.time.Clock()

    fondo = Sprite(
        "src/recursos/fondo.png",
        60, 30
    )

    fondo_estatico = Sprite("src/recursos/fondo-estatico.png", TILES, TILES)

    fondo.cuerpo.x = -(fondo.width - DIMENSIONES_DEL_LIENZO[0]) / 2
    fondo.cuerpo.y = -(fondo.height - DIMENSIONES_DEL_LIENZO[1]) / 2

    posicion_inicial_x = escena.get_rect().center[0] - MEDIDA_DE_TILE / 2
    posicion_inicial_y = escena.get_rect().center[1] - MEDIDA_DE_TILE / 2

    jugador = Jugador(
        posicion_inicial_x, posicion_inicial_y, MEDIDA_DE_TILE, MEDIDA_DE_TILE,
        VELOCIDAD, "src/recursos/jugador.png"
    )

    enemigos = []
    posicion_mouse = pygame.mouse.get_pos()
    movimiento_mouse = False

    for i in range(20):
        x = random.randint(fondo.cuerpo.left, int(fondo.cuerpo.right - MEDIDA_DE_TILE))
        y = random.randint(fondo.cuerpo.top, int(fondo.cuerpo.bottom - MEDIDA_DE_TILE))
        enemigos.append(
            Entidad(
                x, y, MEDIDA_DE_TILE, MEDIDA_DE_TILE,
                VELOCIDAD / 2, "src/recursos/enemigo.png")
        )

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            if evento.type == jugador.controles["click"]:
                print("Click")
            if evento.type == pygame.MOUSEMOTION:
                posicion_mouse = pygame.mouse.get_pos()

        teclas_presionadas = pygame.key.get_pressed()


        if teclas_presionadas[jugador.controles["adelante"]]:
            jugador.mover(posicion_mouse, fondo.cuerpo, -1, enemigos)

        elif teclas_presionadas[jugador.controles["atrás"]]:
            jugador.mover(posicion_mouse, fondo.cuerpo, 1, enemigos)



        escena.blit(fondo_estatico.imagen, fondo_estatico.cuerpo)
        escena.blit(fondo.imagen, fondo.cuerpo)

        for enemigo in enemigos:
            if teclas_presionadas[pygame.K_SPACE]:
                enemigo.mover(jugador.cuerpo.center, fondo.cuerpo, 1, enemigos)
            escena.blit(enemigo.sprite, enemigo.cuerpo)

        escena.blit(jugador.sprite, jugador.cuerpo)

        pygame.display.flip()
        tiempo.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
