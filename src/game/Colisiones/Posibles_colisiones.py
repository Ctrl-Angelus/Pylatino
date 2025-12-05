from src.game.Gestion.Contexto import ContextoDelJuego


def posibles_colisiones(rect, contexto: ContextoDelJuego):
    tiles = contexto.escenario.tile_map.obtener_tiles_cercanos(rect)
    tiles_seguros = 0
    entidades_seguras = 0
    for tile in tiles:
        if tile is None:
            continue
        if not tile.colision or not tile.cuerpo.colliderect(rect):
            tiles_seguros += 1

    for entidad_lista in contexto.entidades:
        if not entidad_lista.cuerpo.colliderect(rect):
            entidades_seguras += 1

    return tiles_seguros == len(tiles) and entidades_seguras == len(contexto.entidades)

def posibles_colisiones_jugador(jugador, contexto: ContextoDelJuego):
    tile_actual = contexto.escenario.tile_map.obtener_tile_actual(jugador.cuerpo)
    if tile_actual is None:
        return False

    tiles = contexto.escenario.tile_map.obtener_tiles_cercanos(jugador.cuerpo)
    tiles_seguros = 0
    entidades_seguras = 0

    for tile in tiles:
        if tile is None:
            continue
        if not tile.colision or not tile.cuerpo.colliderect(jugador.cuerpo):
            tiles_seguros += 1

    for entidad_lista in contexto.entidades:
        if not entidad_lista.cuerpo.colliderect(jugador.cuerpo) or jugador is entidad_lista:
            entidades_seguras += 1

    return tiles_seguros == len(tiles) and entidades_seguras == len(contexto.entidades)