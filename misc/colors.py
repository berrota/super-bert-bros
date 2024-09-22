#Colores

WHITE = (255, 255, 255) #blanco

BLACK = (0, 0, 0) #negro

RED = (255, 0, 0) #rojo

GREEN = (0, 255, 0) #esmeralda

BLUE = (0, 0, 255) #azul

DARK_RED = (45, 0, 0) #granate


# Utilidades

def hex_to_rgb(hex_color:str) -> tuple[int, int, int]:
    """Convertir color en formato hexadecimal a formato RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))