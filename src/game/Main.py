import pygame

from src.game.Gestion.AdministradorDeEntidades import AdministradorDeEntidades
from src.game.Clases.Jugador import Jugador
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Gestion.Controlador import Controlador
from src.game.Gestion.Parametros import FPS, DIMENSIONES_DEL_LIENZO


def main():
    contexto = ContextoDelJuego()

    jugador = Jugador(contexto)

    administrador_de_entidades = AdministradorDeEntidades(contexto, jugador)
    administrador_de_entidades.generar_oleada(20)

    controlador = Controlador(contexto, jugador)

    while contexto.ejecutando:
        for evento in pygame.event.get():
            controlador.verificar_eventos(evento)

        controlador.verificar_controles()

        contexto.escenario.mostrar()

        for entidad in contexto.entidades:
            entidad.mover()
            if 0 <= entidad.cuerpo.right and entidad.cuerpo.left <= DIMENSIONES_DEL_LIENZO[0] and 0 <= entidad.cuerpo.bottom and entidad.cuerpo.top <= DIMENSIONES_DEL_LIENZO[1]:
                contexto.escena.blit(entidad.sprite, entidad.cuerpo)

        contexto.escena.blit(jugador.sprite, jugador.cuerpo)

        pygame.display.flip()
        contexto.reloj.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
