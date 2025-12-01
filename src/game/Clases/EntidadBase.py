import pygame
from pygame import Rect, Surface
from src.game.Gestion.Parametros import MEDIDA_DE_TILE_ESCALADO
from src.game.Gestion.Contexto import ContextoDelJuego


class EntidadBase:
    def __init__(self, posicion_inicial: tuple, velocidad: float, url: str, contexto: ContextoDelJuego):

        self.alto = MEDIDA_DE_TILE_ESCALADO
        self.ancho = MEDIDA_DE_TILE_ESCALADO

        self.url: str = url
        self.imagen: Surface = pygame.image.load(url).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.imagen,
            (
                self.imagen.get_width() * (self.alto / self.imagen.get_width()),
                self.imagen.get_height() * (self.ancho / self.imagen.get_height()),
            )
        )
        rect = self.sprite.get_rect()
        self.cuerpo: Rect = rect.inflate(-10, -10)
        self.velocidad: float = velocidad

        self.cuerpo.move_ip(posicion_inicial)
        self.contexto = contexto
