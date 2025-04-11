import pygame
from typing import Literal

from misc.files import projectile_image_left, projectile_image_right, relres

MAX_PROJECTILES: int = 8

class Projectile:
    def __init__(self, x:int, y:int, direction:Literal["left", "right"]):
        """Inicializar la clase para los proyectiles."""
        
        #Atributos para el movimiento
        self.rect: pygame.Rect = pygame.Rect(x, y, relres(64), relres(y=64))
        self.start_pos: int = x
        self.max_displacement: int = relres(960)
        self.velocity: int = 13
        self.direction: Literal["left", "right"] = direction
        self.image: pygame.Surface = projectile_image_left if direction == "left" else projectile_image_right
    
    def move(self, dt:float) -> None:
        """Moverse constantemente hacia la dirección en la que mira el jugador que lo ha lanzado."""
        
        if self.direction == "left":
            self.rect.x -= self.velocity * dt / 0.016
            
        elif self.direction == "right":
            self.rect.x += self.velocity * dt / 0.016
    
    def is_out_of_bounds(self) -> bool:
        """Verificar si el proyectil se ha movido más de lo que debe."""
        return abs(self.rect.x - self.start_pos) > self.max_displacement
    
    def draw(self, screen:pygame.Surface) -> None:
        """Dibujar el proyectil en pantalla."""
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def draw_hitboxes(self, screen:pygame.Surface) -> None:
        """Dibujar las hitboxes de los proyectiles en pantalla."""
        
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)


def handle_projectile_logic(players: pygame.sprite.Group, platforms: tuple) -> None:
    """Maneja la lógica de los proyectiles."""
    player1, player2 = players
    
    #Proyectiles de jugador 1
    for projectile in player1.projectiles:

        #Hacer que haga daño
        if projectile.rect.colliderect(player2.rect):
            player2.get_hit(projectile.direction, player1.projectile_damage)
            player1.projectiles.remove(projectile)
        
        #Colisión con la plataforma grande
        if projectile.rect.colliderect(platforms[0]):
            player1.projectiles.remove(projectile)

    #Proyectiles de jugador 2
    for projectile in player2.projectiles:

        #Hacer que haga daño
        if projectile.rect.colliderect(player1.rect):
            player1.get_hit(projectile.direction, player2.projectile_damage)
            player2.projectiles.remove(projectile)
        
        #Colisión con la plataforma grande
        if projectile.rect.colliderect(platforms[0]):
            player2.projectiles.remove(projectile)
    
    if len(player1.projectiles) > MAX_PROJECTILES: #Máximos proyectiles permitidos
                player1.projectiles.pop(0)

    if len(player2.projectiles) > MAX_PROJECTILES: #Máximos proyectiles permitidos
                player2.projectiles.pop(0)