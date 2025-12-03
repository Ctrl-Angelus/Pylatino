
from src.game.Sprites.SpriteSheet import SpriteSheet
from src.game.Tiles.TileMap import TileMap


class Escenario:
    def __init__(self, contexto):
        self.contexto = contexto

        self.tile_map = TileMap("src/recursos/tilemap/tilemap-1.txt", "src/recursos/tilemap/tileset2.png", contexto)

        self.fondo_estatico = SpriteSheet("src/recursos/fondo-estatico.png")
        self.fondo_estatico.generar_frames(4, 2, (60, 60), 1)
        self.fondo_estatico.iniciar_animacion()


    def mostrar(self):
        sprite = self.fondo_estatico.obtener_sprite_actual()
        self.contexto.escena.blit(
            sprite.imagen,
            sprite.cuerpo)

        self.fondo_estatico.animacion(0)
        self.tile_map.mostrar()
