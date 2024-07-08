import pygame

from misc.files import font, title_font

def draw_pause_screen(surface, screen_width, screen_height):
    """Dibujar el menú de pausa."""

    #Superficies
    pygame.draw.rect(surface, (128, 128, 128, 150), (0, 0, screen_width, screen_height))
    pygame.draw.rect(surface, "black", (200, 150, 1500, 150), 0, 10)

    #Botones
    resume = pygame.draw.rect(surface, "white", (300, 450, 600, 150), 0, 10)
    quit = pygame.draw.rect(surface, "white", (1000, 450, 600, 150), 0, 10)
    change_characters = pygame.draw.rect(surface, "white", (300, 700, 600, 150), 0, 10)
    change_volume = pygame.draw.rect(surface, "white", (1000, 700, 600, 150), 0, 10)

    #Texto
    surface.blit(title_font.render("Juego pausado.", True, "white"), (750, 190))
    surface.blit(font.render("Volver", True, "black"), (520, 505))
    surface.blit(font.render("Cerrar", True, "black"), (1250, 505))
    surface.blit(font.render("Cambiar personajes", True, "black"), (435, 755))
    surface.blit(font.render("Ajustar volumen", True, "black"), (1180, 755))

    #Devolver los botones para que se puedan dibujar en pantalla
    return resume, quit, change_characters, change_volume