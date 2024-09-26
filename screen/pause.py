import pygame

from misc.colors import *
from misc.files import font, title_font
from misc.translator import translate

def draw_pause_screen(surface, screen_width, screen_height) -> tuple[pygame.Rect, pygame.Rect, pygame.Rect, pygame.Rect, pygame.Rect]:
    """Dibujar el menú de pausa y sus botones."""

    #Superficies
    pygame.draw.rect(surface, (128, 128, 128, 150), (0, 0, screen_width, screen_height))
    title_rect = pygame.draw.rect(surface, BLACK, (200, 50, 1500, 150), 0, 10)
    
    #Botones
    resume_rect = pygame.draw.rect(surface, WHITE, (300, 350, 600, 150), 0, 10)
    quit_rect = pygame.draw.rect(surface, WHITE, (1000, 350, 600, 150), 0, 10)
    change_characters_rect = pygame.draw.rect(surface, WHITE, (300, 600, 600, 150), 0, 10)
    change_volume_rect = pygame.draw.rect(surface, WHITE, (1000, 600, 600, 150), 0, 10)
    options_rect = pygame.draw.rect(surface, WHITE, (350, 850, 1200, 150), 0, 10)

    #Texto
    title_text = title_font.render(translate("pause.title"), True, WHITE)
    resume_text = font.render(translate("pause.back"), True, BLACK)
    quit_text = font.render(translate("pause.quit"), True, BLACK)
    change_character_text = font.render(translate("pause.change_character"), True, BLACK)
    adjust_volume_text = font.render(translate("pause.adjust_volume"), True, BLACK)
    options_text = font.render(translate("pause.options"), True, BLACK)
    
    #Centrar título
    title_text_rect = title_text.get_rect(center=(title_rect.center))
    surface.blit(title_text, title_text_rect)
    
    #Centrar texto de botones
    resume_text_rect = resume_text.get_rect(center=resume_rect.center)
    quit_text_rect = quit_text.get_rect(center=quit_rect.center)
    change_character_text_rect = change_character_text.get_rect(center=change_characters_rect.center)
    adjust_volume_text_rect = adjust_volume_text.get_rect(center=change_volume_rect.center)
    options_text_rect = options_text.get_rect(center=options_rect.center)
    
    #Dibujar botones en pantalla
    surface.blit(resume_text, resume_text_rect)
    surface.blit(quit_text, quit_text_rect)
    surface.blit(change_character_text, change_character_text_rect)
    surface.blit(adjust_volume_text, adjust_volume_text_rect)
    surface.blit(options_text, options_text_rect)
    
    #Devolver los botones para que se puedan dibujar en pantalla
    return resume_rect, quit_rect,  change_characters_rect, change_volume_rect, options_rect