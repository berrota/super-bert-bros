import pygame

from misc.files import platform_image, small_platform_image

class Platform:
    def __init__(self, x, y, w, h, size):
        """Inicializa la clase de las plataformas."""
        
        # Diferenciar dos tipos de plataformas: grandes (big) y pequeñas (small)
        
        if size == "big":
            self.image = platform_image
            self.rect = pygame.Rect(x, y, w, h//4)
            
        elif size == "small":
            self.image = small_platform_image
            self.rect = pygame.Rect(x, y, w, h)
        
        
    def draw(self, screen):
        """Dibuja las plataformas en pantalla."""
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    
    def draw_hitboxes(self, screen):
        """Dibuja las hitboxes de las plataformas en pantalla."""
        
        pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)