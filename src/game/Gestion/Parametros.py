import tkinter


raiz = tkinter.Tk() # Una instancia de Tkinter que se usará para determinar las dimensiones de la aplicación

raiz.withdraw() # Evita que se muestre la ventana

ALTO_DE_LA_VENTANA: float = raiz.winfo_screenheight() * 0.9 # Se obtiene el 90% del alto de la ventana desde Tkinter

ANCHO_DE_LA_VENTANA: float = ALTO_DE_LA_VENTANA # La ventana tiene mismo alto y ancho

# Se almacenan las dimensiones en una tupla para evitar alteraciones posteriores
DIMENSIONES_DEL_LIENZO: tuple = (
    ANCHO_DE_LA_VENTANA,
    ALTO_DE_LA_VENTANA
)

TITULO = "Proyecto Pylatino"

FPS: int = 60

CANTIDAD_DE_TILES = 15

MEDIDA_DE_TILE_ORIGINAL = 16 # Cada Tile mide 16x16 pixeles

MEDIDA_DE_TILE_ESCALADO: float = ALTO_DE_LA_VENTANA / CANTIDAD_DE_TILES # Se divide el tamaño de la ventana entre la cantidad de tiles

VELOCIDAD: float = (10 * MEDIDA_DE_TILE_ESCALADO) / FPS # La velocidad son la cantidad de tiles que se mueve el personaje entre los fps cada segundo

