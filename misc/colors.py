#Colores

WHITE = (255, 255, 255) #blanco

BLACK = (0, 0, 0) #negro

RED = (255, 0, 0) #rojo

GREEN = (0, 255, 0) #esmeralda

LIME = (50, 200, 50) #lima

BLUE = (0, 0, 255) #azul

DARK_RED = (45, 0, 0) #granate


# Utilidades

def hex_to_rgb(hex_color:str) -> tuple[int, int, int]:
    """Convierte códigos de color en formato hexadecimal a formato RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    """Convierte códigos de color en formato RGB a formato hexadecimal."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)