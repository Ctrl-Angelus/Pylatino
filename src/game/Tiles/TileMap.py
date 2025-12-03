from typing import Optional

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

        self.tile_set = TileSet(tile_set_url, MEDIDA_DE_TILE_ORIGINAL, MEDIDA_DE_TILE_ORIGINAL, 1)

        self.tiles = []

        self.height = len(self.datos) * int(MEDIDA_DE_TILE_ESCALADO)
        self.width = len(self.datos[0]) * int(MEDIDA_DE_TILE_ESCALADO)

        self.posicion_inicial = (
            -(self.width - DIMENSIONES_DEL_LIENZO[0]) / 2,
            -(self.height - DIMENSIONES_DEL_LIENZO[1]) / 2,
        )

        posicion_y = self.posicion_inicial[1]
        for fila in range(len(self.datos)):
            posicion_x = self.posicion_inicial[0]
            fila_actual = []
            for columna in range(len(self.datos[fila])):

                lista = self.tile_set.tiles
                indice = int(self.datos[fila][columna]) - 1
                imagen_nuevo_tile = lista[0][indice]
                nuevo_tile = Tile(
                    None,
                    (1, 1),
                    imagen_nuevo_tile.copy(),
                    int(posicion_x),
                    int(posicion_y),
                    contexto,
                    f"{fila} - {columna}"
                )

                fila_actual.append(nuevo_tile)
                posicion_x += int(MEDIDA_DE_TILE_ESCALADO)

            self.tiles.append(fila_actual)
            posicion_y += int(MEDIDA_DE_TILE_ESCALADO)

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
                    self.contexto.escena.blit(tile.imagen, tile.obtener_posicion_visual())

    def obtener_tile_actual(self, entidad) -> Optional[Tile]:
        x_mundo = entidad.cuerpo.centerx
        y_mundo = entidad.cuerpo.centery

        col = int((x_mundo - self.posicion_inicial[0]) // MEDIDA_DE_TILE_ESCALADO)
        fila = int((y_mundo - self.posicion_inicial[1]) // MEDIDA_DE_TILE_ESCALADO)

        if 0 <= fila < len(self.tiles) and 0 <= col < len(self.tiles[0]):
            return self.tiles[fila][col]
        else:
            return None