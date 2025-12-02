from pygame import Rect

from src.game.Gestion.Parametros import MEDIDA_DE_TILE_ESCALADO, DIMENSIONES_DEL_LIENZO
from src.game.Tile import Tile


class TileMap:
    def __init__(self, url: str, contexto):
        self.contexto = contexto

        self.url = url
        archivo = open(url).read().split()
        self.datos = []
        for linea in archivo:
            self.datos.append(linea.split(","))

        self.tile_set = {
            "1": "src/recursos/tilemap/tiles/tierra.png",
            "2": "src/recursos/tilemap/tiles/agua.png"
        }

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
            for i in range(len(linea)):
                ruta_tile = self.tile_set[linea[i]]
                fila.append(Tile(ruta_tile, (1, 1), None, int(x), int(y)))
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
            for i in range(len(linea)):
                self.contexto.escena.blit(linea[i].imagen, linea[i].cuerpo)