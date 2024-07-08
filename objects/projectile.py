import pygame
from misc.files import projectile_image_left, projectile_image_right

class Projectile:
    def __init__(self, x, y, direction, players):
        """Inicializar la clase para los proyectiles."""
        
        #Atributos para el movimiento
        self.rect = pygame.Rect(x, y, 64, 64)
        self.start_pos = x
        self.max_displacement = 960
        self.velocity = 13
        self.direction = direction
        
        if self.direction == "left":
            self.image = projectile_image_left
            
        elif self.direction == "right":
            self.image = projectile_image_right
            
    
    def draw(self, screen):
        """Dibujar el proyectil en pantalla."""
        
        self.move()
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def move(self):
        """Moverse constantemente hacia la dirección en la que mira el jugador que lo ha lanzado."""
        
        if self.direction == "left":
            self.rect.x -= self.velocity
            
        elif self.direction == "right":
            self.rect.x += self.velocity
    
    def draw_hitboxes(self, screen):
        """Dibujar las hitboxes de los proyectiles en pantalla."""
        
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)