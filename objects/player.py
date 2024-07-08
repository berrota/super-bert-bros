import pygame
from typing import Literal

from misc.characters import *
from misc.files import *

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, character:dict, name:str):
        
        super().__init__()

        #Atributos (las stats se encuentran en misc/characters.py)
        self.name = name
        
        self.dx = 0
        self.dy = 0
        
        self.velocity = character["velocity"]
        self.jump_velocity = character["jump_velocity"]
        self.terminal_velocity = character["terminal_velocity"]
        self.gravity = character["gravity"]
        self.hp = character["health"]
        self.projectile_damage = character["projectile_damage"]
        self.lives = 2 #Son vidas restantes, no confundir con vidas totales (en total serían 3)
        self.weight = character["weight"]

        #Cosas para los ataques melee (por ahora es inútil)
        self.attacking = False
        self.damage = character["damage"]
        self.crit_chance = character["crit_chance"]

        #Declarar sprites
        self.character = character
        self.status = "idle"
        self.facing = "right"
        self.icon = character["icon"]
        self.walking_sprites_left = character["walking_sprites_left"]
        self.walking_sprites_right = character["walking_sprites_right"]
        self.jumping_sprites_left = character["jumping_sprites_left"]
        self.jumping_sprites_right = character["jumping_sprites_right"]
        self.idle_sprite_left = character["idle_sprite_left"]
        self.idle_sprite_right = character["idle_sprite_right"]
        self.attack_sprite_left = character["attack_sprite_left"]
        self.attack_sprite_right = character["attack_sprite_right"]
        self.damage_sprite_left = character["damage_sprite_left"]
        self.damage_sprite_right = character["damage_sprite_right"]
        self.current_sprites = self.idle_sprite_right
        self.current_sprite = 0
        self.image = self.current_sprites[self.current_sprite]

        #Hitbox
        self.rect = pygame.Rect(x, y, self.idle_sprite_left[0].get_width(), self.idle_sprite_left[0].get_height())
        self.rect.topleft = [x, y]
    
    
    def move(self, direction:Literal["left", "right"]):
        """Función para moverse."""
        
        #Actualizar sprites dependiendo de la dirección del jugador
        if direction > 0:
            self.facing = "right" #mirando a la derecha
            self.status = "walking" #caminando
            
        elif direction < 0:
            self.facing = "left" #mirando a la izquierda
            self.status = "walking" #caminando
            
        #No moverse si la dirección es cero
        else:
            self.status = "idle"

        #Dar nuevo valor a la variable dx
        self.dx = direction * self.velocity
        

    def jump(self, platforms:list):
        """Función para saltar."""
        
        #Dar valor 0 a dy si está tocando una plataforma
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.dy = 0
                return
        
        #Saltar solo si dy equivale a 0
        if self.dy == 0:
            self.dy -= self.jump_velocity
            self.status = "jumping"


    def animate(self):
        """Animaciones."""
        #Mirando a la izquierda
        if self.facing == "left":

            #Caminando
            if self.status == "walking":
                self.current_sprites = self.walking_sprites_left
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.current_sprites):
                    self.current_sprite = 0
                
                self.image = self.current_sprites[int(self.current_sprite)]
        
            #Saltando
            if self.status == "jumping":
                self.current_sprites = self.jumping_sprites_left
                self.current_sprite += 0.15

                if self.current_sprite >= len(self.current_sprites):
                    self.current_sprite = 0
                
                self.image = self.current_sprites[int(self.current_sprite)]
            
            #Idle (estando)
            if self.status == "idle":
                self.image = self.idle_sprite_left[0]
            
            #Recibiendo daño
            if self.status == "damaged":
                self.image = self.damage_sprite_left[0]
            
            #Atacando
            if self.status == "attacking":
                self.image = self.attack_sprite_left[0]

        #Mirando a la derecha
        elif self.facing == "right":

            #Caminando
            if self.status == "walking":
                self.current_sprites = self.walking_sprites_right
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.current_sprites):
                    self.current_sprite = 0
                
                self.image = self.current_sprites[int(self.current_sprite)]
        
            #Saltando
            if self.status == "jumping":
                self.current_sprites = self.jumping_sprites_right
                self.current_sprite += 0.15

                if self.current_sprite >= len(self.current_sprites):
                    self.current_sprite = 0
                
                self.image = self.current_sprites[int(self.current_sprite)]
            
            #Idle (estando)
            if self.status == "idle":
                self.image = self.idle_sprite_right[0]

            #Recibiendo daño
            if self.status == "damaged":
                self.image = self.damage_sprite_right[0]
            
            #Atacando
            if self.status == "attacking":
                self.image = self.attack_sprite_right[0]
    
    
    def get_hit(self, side:Literal["left", "right"]):
        """Función para recibir daño, hace funcionar el empuje y reproduce el sonido de daño."""
        
        pygame.mixer.Sound.play(damage_sound)
        
        self.status = "damaged"
        
        if side == "left":
            self.dx = -((self.character["health"] - self.hp)) * self.weight
            
        elif side == "right":
            self.dx = ((self.character["health"] - self.hp)) * self.weight
            
        self.dy = -1 * ((self.character["health"] - self.hp) // 10) * self.weight


    def draw_hitboxes(self, screen:pygame.display.set_mode):
        """Dibujar la hitbox del jugador."""
        
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        
        
    def update(self, platforms:list):
        """Actualiza la posición del jugador, y hace funcionar las colisiones."""
        
        #Actualizar la posición usando dx para movimiento horizontal y dy para movimiento vertical, la gravedad y la velodad terminal también son factores.
        self.dy = min(self.terminal_velocity, self.dy + self.gravity)
        
        self.rect.x += self.dx
        self.rect.y += self.dy

        #Manejar colisiones
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.dy > 0:
                    self.dy = 0
                    self.rect.bottom = platform.rect.top
        
        #Comprobar qué acción está realizando el jugador
        if self.status != "damaged" and self.status != "attacking":
            if self.dy != 0:
                self.status = "jumping"
                
            else:
                if self.dx != 0:
                    self.status = "walking"
                    
                else:
                    self.status = "idle"
    
                
        #Animar al jugador (vamos tú puedes!!!)
        self.animate()