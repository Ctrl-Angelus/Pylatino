import pygame

from src.game.Gestion.AdministradorDeEntidades import AdministradorDeEntidades
from src.game.Clases.Jugador import Jugador
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Gestion.Controlador import Controlador
from src.game.Gestion.Parametros import FPS, DIMENSIONES_DEL_LIENZO


def main():
    contexto = ContextoDelJuego()

    jugador = Jugador(contexto)
    contexto.jugador = jugador

    administrador_de_entidades = AdministradorDeEntidades(contexto)
    contexto.administrador_de_entidades = administrador_de_entidades
    contexto.administrador_de_entidades.generar_oleada(10)
    contexto.entidades.append(jugador)

    controlador = Controlador(contexto, jugador)

    pygame.mixer.music.load("src/recursos/audio/musica-fondo.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    menu_original = pygame.image.load("src/recursos/menu.png")

    menu = pygame.transform.scale(
        menu_original,
        (
            menu_original.get_width() * DIMENSIONES_DEL_LIENZO[0] / menu_original.get_width(),
            menu_original.get_height() * DIMENSIONES_DEL_LIENZO[1] / menu_original.get_height()
        )
    )


    while contexto.ejecutando:

        if contexto.menu_activo:
            contexto.escena.blit(menu, (0, 0))
            texto = contexto.fuente.render("Presione ENTER para continuar", True, (255, 255, 255))
            contexto.escena.blit(texto, (
                DIMENSIONES_DEL_LIENZO[0] / 2 - texto.get_width() / 2, DIMENSIONES_DEL_LIENZO[1] * 0.8
            ))
            pygame.display.flip()
            contexto.reloj.tick(FPS)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    contexto.terminar_game_loop()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        contexto.menu_activo = False


            continue

        for evento in pygame.event.get():

            controlador.verificar_eventos(evento)


        controlador.verificar_controles()

        contexto.escenario.mostrar()

        for entidad in contexto.entidades:
            if entidad is jugador:
                continue
            entidad.actualizar_muerte()
            entidad.movimiento()
            entidad.actualizar()

            if entidad.es_visible():
                entidad.mostrar()


        jugador.actualizar_muerte()
        jugador.mostrar()
        jugador.actualizar()
        jugador.actualizar_disparo()

        for proyectil in contexto.proyectiles:
            proyectil.mover()
            proyectil.mostrar()

        tamaño = contexto.fuente.get_height()
        imagen_1 = pygame.image.load("src/recursos/interfaz/barra-vida-2.png")

        barra_vida = pygame.transform.scale(
            imagen_1,
            (
                imagen_1.get_width() * tamaño / imagen_1.get_height(),
                imagen_1.get_height() * tamaño / imagen_1.get_height()
            )
        )
        imagen_2 = pygame.image.load("src/recursos/interfaz/barra-vida-1.png")
        total = imagen_2.get_width() * tamaño / imagen_2.get_height()
        porcentaje = jugador.vida / jugador.vida_total
        barra_vida_contenido_original = pygame.transform.scale(
            imagen_2,
            (
                total,
                imagen_1.get_height() * tamaño / imagen_1.get_height()
            )
        )

        barra_vida_contenido = pygame.transform.scale(
            imagen_2,
            (
                int(total * porcentaje),
                imagen_1.get_height() * tamaño / imagen_1.get_height()
            )
        )

        contexto.escena.blit(barra_vida_contenido, (barra_vida.get_width() - barra_vida_contenido_original.get_width(), 10))
        contexto.escena.blit(barra_vida, (10, 10))


        contexto.escena.blit(
            contexto.fuente.render(f"Enemigos: {len(contexto.entidades) - 1}", True, (255, 255, 255)),
            (10, DIMENSIONES_DEL_LIENZO[1] - contexto.fuente.get_height() - 10)
        )


        pygame.display.flip()
        contexto.reloj.tick(FPS)

    open("src/recursos/estadisticas/estadisticas.txt", "w")
    pygame.quit()


if __name__ == "__main__":
    main()
