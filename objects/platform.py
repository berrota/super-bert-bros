import pygame
from typing import Literal

from misc.files import big_platform_image, small_platform_image

class Platform:
    """Objeto para las plataformas. Existen dos tipos: Grandes (la principal) y pequeñas (las otras dos que están más elevadas)."""
    
    def __init__(self, dimensions: tuple, size: Literal["big", "small"]):
        #Diferenciar entre dos tipos de plataformas: grandes (big) y pequeñas (small)
        x, y, w, h = dimensions
        self.size: Literal["big", "small"] = size
        
        self.image: pygame.Surface = big_platform_image if size == "big" else small_platform_image
        self.rect: pygame.Rect = pygame.Rect(x, y, w, h // 4) if size == "big" else pygame.Rect(x, y, w, h)
        
    def draw(self, screen:pygame.Surface) -> None:
        """Dibuja las plataformas en pantalla."""
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    
    def draw_hitboxes(self, screen:pygame.Surface) -> None:
        """Dibuja las hitboxes de las plataformas en pantalla."""
        pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)