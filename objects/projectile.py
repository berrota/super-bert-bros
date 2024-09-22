import pygame
from typing import Literal

from misc.files import projectile_image_left, projectile_image_right

class Projectile:
    def __init__(self, x:int, y:int, direction:Literal["left", "reight"]):
        """Inicializar la clase para los proyectiles."""
        
        #Atributos para el movimiento
        self.rect: pygame.Rect = pygame.Rect(x, y, 64, 64)
        self.start_pos: int = x
        self.max_displacement: int = 960
        self.velocity: int = 13
        self.direction: Literal["left", "reight"] = direction
        self.image: pygame.Surface = None
        
        if self.direction == "left":
            self.image = projectile_image_left
            
        elif self.direction == "right":
            self.image = projectile_image_right
            
    
    def draw(self, screen:pygame.Surface) -> None:
        """Dibujar el proyectil en pantalla."""
        
        self.move()
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def move(self) -> None:
        """Moverse constantemente hacia la dirección en la que mira el jugador que lo ha lanzado."""
        
        if self.direction == "left":
            self.rect.x -= self.velocity
            
        elif self.direction == "right":
            self.rect.x += self.velocity
    
    def draw_hitboxes(self, screen:pygame.Surface) -> None:
        """Dibujar las hitboxes de los proyectiles en pantalla."""
        
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)