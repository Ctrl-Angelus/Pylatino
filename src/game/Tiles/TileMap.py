
from pygame import Rect

from src.game.Gestion.Parametros import MEDIDA_DE_TILE_ESCALADO, DIMENSIONES_DEL_LIENZO, MEDIDA_DE_TILE_ORIGINAL
from src.game.Tiles.Tile import Tile
from src.game.Tiles.TileSet import TileSet


class TileMap:
    def __init__(self, tile_map_url: str, tile_set_url: str, contexto):
        self.contexto = contexto

        self.tile_map_url = tile_map_url
        archivo = open(tile_map_url).read().split()
        self.datos = []
        for linea in archivo:
            self.datos.append(linea.split(","))

        self.tile_set = TileSet(contexto, tile_set_url, MEDIDA_DE_TILE_ORIGINAL, MEDIDA_DE_TILE_ORIGINAL, 1)

        self.tiles = []

        self.height = len(self.datos) * int(MEDIDA_DE_TILE_ESCALADO)
        self.width = len(self.datos[0]) * int(MEDIDA_DE_TILE_ESCALADO)

        self.posicion_inicial = (
            -(self.width - DIMENSIONES_DEL_LIENZO[0]) / 2,
            -(self.height - DIMENSIONES_DEL_LIENZO[1]) / 2,
        )

        y = self.posicion_inicial[1]
        for linea in self.datos:
            x = self.posicion_inicial[0]
            fila = []
            for tile in linea:
                indice = int(tile) - 1
                lista = self.tile_set.tiles
                tile = lista[0][indice]
                fila.append(Tile(None, (1, 1), tile.copy(), int(x), int(y), contexto))
                x += int(MEDIDA_DE_TILE_ESCALADO)
            self.tiles.append(fila)
            y += int(MEDIDA_DE_TILE_ESCALADO)

        self.borde = Rect(
            self.posicion_inicial[0],
            self.posicion_inicial[1],
            self.width,
            self.height
        )

    def mostrar(self):
        for linea in self.tiles:
            for tile in linea:
                if tile.es_visible():
                    self.contexto.escena.blit(tile.imagen, (tile.cuerpo.x - self.contexto.offset[0], tile.cuerpo.y - self.contexto.offset[1]))