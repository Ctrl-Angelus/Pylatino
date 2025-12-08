from typing import Optional

from pygame import Rect

from src.game.Gestion.Parametros import MEDIDA_DE_TILE_ESCALADO, DIMENSIONES_DEL_LIENZO, MEDIDA_DE_TILE_ORIGINAL
from src.game.Tiles.Tile import Tile, TileCuracion, TileMunicion
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
            -(self.height - DIMENSIONES_DEL_LIENZO[1]),
        )

        posicion_y = self.posicion_inicial[1]
        for fila in range(len(self.datos)):
            posicion_x = self.posicion_inicial[0]
            fila_actual = []
            for columna in range(len(self.datos[fila])):

                lista = self.tile_set.tiles
                material = int(self.datos[fila][columna])
                if material == 0:
                    fila_actual.append(None)
                    posicion_x += int(MEDIDA_DE_TILE_ESCALADO)
                    continue

                indice =  material - 1
                colision = True if (material in (1, 2, 3, 5, 6, 12, 13)) else False
                accion = True if material in (10, 13) else False

                imagen_nuevo_tile = lista[0][indice]

                if material == 10:
                    nuevo_tile = TileCuracion(
                        None,
                        (1, 1),
                        imagen_nuevo_tile.copy(),
                        int(posicion_x),
                        int(posicion_y),
                        contexto,
                        f"{fila} - {columna}",
                        colision,
                        accion,
                        lista[0][8].copy()
                    )
                elif material == 13:
                    nuevo_tile = TileMunicion(
                        None,
                        (1, 1),
                        imagen_nuevo_tile.copy(),
                        int(posicion_x),
                        int(posicion_y),
                        contexto,
                        f"{fila} - {columna}",
                        colision,
                        accion,
                        lista[0][13].copy()
                    )
                else:
                    nuevo_tile = Tile(
                        None,
                        (1, 1),
                        imagen_nuevo_tile.copy(),
                        int(posicion_x),
                        int(posicion_y),
                        contexto,
                        f"{fila} - {columna}",
                        colision,
                        accion,
                        imagen_nuevo_tile.copy()
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
                if tile is None:
                    continue
                if tile.es_visible():
                    self.contexto.escena.blit(tile.imagen, tile.obtener_posicion_visual())

    def obtener_tile_actual(self, rect) -> Optional[Tile]:
        columna, fila = self.calcular_coordenada_de_tile(rect)

        if self.verificar_coordenada(fila, columna):
            return self.tiles[fila][columna]
        else:
            return None

    def obtener_tiles_cercanos(self, rect):
        columna, fila = self.calcular_coordenada_de_tile(rect)

        tiles = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.verificar_coordenada(fila + i, columna + j):
                    tiles.append(self.tiles[fila + i][columna + j])

        return tiles

    def calcular_coordenada_de_tile(self, rect) -> tuple:
        x_mundo = rect.centerx
        y_mundo = rect.centery

        columna = int((x_mundo - self.posicion_inicial[0]) // MEDIDA_DE_TILE_ESCALADO)
        fila = int((y_mundo - self.posicion_inicial[1]) // MEDIDA_DE_TILE_ESCALADO)

        return columna, fila

    def verificar_coordenada(self, fila, columna) -> bool:
        fila_dentro_de_limites = 0 <= fila < len(self.tiles)
        columna_dentro_de_limites = 0 <= columna < len(self.tiles[0])

        return fila_dentro_de_limites and columna_dentro_de_limites