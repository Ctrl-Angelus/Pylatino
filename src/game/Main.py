import pygame
import random

from src.game.Clases.Entidades import Jugador
from src.game.Parametros import *
from src.game.Clases.Sprite import Sprite
from src.game.Clases.Entidades import Enemigo


def main():
    pygame.init()

    pygame.display.set_caption(TITULO)

    escena = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
    tiempo = pygame.time.Clock()

    entidades = []

    fondo = Sprite("src/recursos/fondo.png", None)

    fondo.cuerpo.x = -(fondo.width - DIMENSIONES_DEL_LIENZO[0]) / 2
    fondo.cuerpo.y = -(fondo.height - DIMENSIONES_DEL_LIENZO[1]) / 2

    fondo_estatico = Sprite("src/recursos/fondo-estatico.png", (TILES, TILES))

    posicion_inicial_x = escena.get_rect().center[0] - MEDIDA_DE_TILE / 2
    posicion_inicial_y = escena.get_rect().center[1] - MEDIDA_DE_TILE / 2

    jugador = Jugador(
        (posicion_inicial_x, posicion_inicial_y),
        MEDIDA_DE_TILE, MEDIDA_DE_TILE,
        VELOCIDAD,
        "src/recursos/jugador.png"
    )

    objetivos = [jugador.cuerpo.topleft, jugador.cuerpo.topright, jugador.cuerpo.bottomleft, jugador.cuerpo.bottomright]

    for i in range(20):
        x_aleatoria = random.randint(fondo.cuerpo.left, int(fondo.cuerpo.right - MEDIDA_DE_TILE))
        y_aleatoria = random.randint(fondo.cuerpo.top, int(fondo.cuerpo.bottom - MEDIDA_DE_TILE))
        entidades.append(
            Enemigo(
                (x_aleatoria, y_aleatoria),
                MEDIDA_DE_TILE, MEDIDA_DE_TILE,
                VELOCIDAD / 2,
                "src/recursos/enemigo.png",
                objetivos)
        )

    posicion_mouse = pygame.mouse.get_pos()

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
            jugador.mover(posicion_mouse, fondo.cuerpo, -1, entidades)

        elif teclas_presionadas[jugador.controles["atrás"]]:
            jugador.mover(posicion_mouse, fondo.cuerpo, 1, entidades)



        escena.blit(fondo_estatico.imagen, fondo_estatico.cuerpo)
        escena.blit(fondo.imagen, fondo.cuerpo)

        for entidad in entidades:
            entidad.mover(fondo.cuerpo, 1, entidades)
            escena.blit(entidad.sprite, entidad.cuerpo)

        escena.blit(jugador.sprite, jugador.cuerpo)

        pygame.display.flip()
        tiempo.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
