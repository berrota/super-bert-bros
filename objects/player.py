import pygame
import time

from typing import Literal

from objects.projectile import Projectile

from misc.characters import *
from misc.files import *

pygame.init()

class Player(pygame.sprite.Sprite):
    """Objeto para el jugador y sus atributos. Aquí se maneja la mayoría de la lógica del movimiento y otras mecánicas del jugador."""
    
    def __init__(self, x:int, y:int, character:dict, name:str, color):
        super().__init__()

        #Atributos (las stats se encuentran en misc/characters.py)
        self.name: str = name
        self.color = color
        
        self.dx: float = 0
        self.dy: float = 0
        
        self.jumping: bool = False
        self.on_ground: bool = False
        self.double_jump_used = False
        self.jump_buffer_time: float = 0
        self.jump_buffer_duration: float = 0.1

        self.attacking: bool = False
        self.attack_cooldown: float = 0.5
        self.attack_timer: float = 0
        
        self.projectiles: list[Projectile] = []
        self.projectile_cooldown: int = 25
        self.projectile_timer: float = 0
        
        self.shooting_frame_duration: int = 15
        self.shooting_frame_timer: float = 0
        
        self.damage_frame_duration: int = 8
        self.damage_frame_timer: float = 0
        
        #Algunos valores se dividen por 0.016 porque el valor inicial estaba pensado para 60 FPS (1/60=~0.016), y con la adición del delta time los valores se vuelven inconsistentes
        self.velocity: float = character["velocity"] / 0.016
        self.jump_velocity: float = character["jump_velocity"] / 0.016
        self.terminal_velocity: float = character["terminal_velocity"] / 0.016
        self.gravity: float = character["gravity"] / 0.016
        self.hp: int = character["health"]
        self.damage: int = character["damage"]
        self.crit_chance: float = character["crit_chance"]
        self.projectile_damage: int = character["projectile_damage"]
        self.lives: int = 2 #Son vidas restantes, no confundir con vidas totales (en total serían 3)
        self.kb_factor: float = (character["weight"] ** -1) / 0.016

        #Declarar sprites
        self.character: dict = character
        self.status: Literal["idle", "jumping", "walking", "shooting", "damaged"] = "idle"
        self.facing: Literal["left", "right"] = "right"
        self.icon: pygame.Surface = character["icon"]
        self.walking_sprites_left: list = character["walking_sprites_left"]
        self.walking_sprites_right: list = character["walking_sprites_right"]
        self.jumping_sprites_left: list = character["jumping_sprites_left"]
        self.jumping_sprites_right: list = character["jumping_sprites_right"]
        self.idle_sprite_left: list = character["idle_sprite_left"]
        self.idle_sprite_right: list = character["idle_sprite_right"]
        self.attack_sprite_left: list = character["attack_sprite_left"]
        self.attack_sprite_right: list = character["attack_sprite_right"]
        self.damage_sprite_left: list = character["damage_sprite_left"]
        self.damage_sprite_right: list = character["damage_sprite_right"]
        self.current_sprites: list = self.idle_sprite_right
        self.current_sprite: float = 0
        self.image: pygame.Surface = self.current_sprites[self.current_sprite]

        #Hitbox
        self.rect: pygame.Rect = pygame.Rect(x, y, self.idle_sprite_left[0].get_width(), self.idle_sprite_left[0].get_height())
        self.rect.topleft = [x, y]
    
    
    def move(self, direction:Literal["left", "right"]) -> None:
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
        

    def jump(self) -> None:
        """Función para saltar."""

        if self.on_ground: #saltos normales desde el suelo
            self.dy -= self.jump_velocity
            self.on_ground = False
            self.jumping = True
        elif not self.double_jump_used and not self.on_ground: #saltos dobles, con mayor impulso vertical para contrarestar la gravedad
            self.dy = -self.jump_velocity
            self.double_jump_used = True
            self.jumping = True
        else:
            self.buffer_jump() #si no se cumple ninguna de estas condiciones, llevar a cabo el buffer del salto
            
    
    def buffer_jump(self) -> None:
        """Almacena el momento en el que el espacio fue presionado para el jump buffering."""
        self.jump_buffer_time = time.time()
       
        
    def apply_jump_buffer(self) -> None:
        """Aplicar la lógica del jump buffering."""
        current_time = time.time()
        
        #Revisar si el tiempo pasado es menor o igual a 0.1 segundos (100 ms)
        if current_time - self.jump_buffer_time <= self.jump_buffer_duration and self.on_ground:
            self.jump()
            self.jump_buffer_time = 0


    def animate(self, dt:float) -> None:
        """Animaciones."""
        #Temporizador de la duración de la animación de disparo
        if self.shooting_frame_timer > 0:
            self.status = "shooting"
            self.shooting_frame_timer -= dt / 0.016
        else:
            if self.status == "shooting":
                self.status = "idle"
        
        if self.damage_frame_timer > 0:
            self.status = "damaged"
            self.damage_frame_timer -= dt / 0.016 ############################################################
        else:
            if self.status == "damaged":
                self.status = "idle"
        
        #Mirando a la izquierda
        if self.facing == "left":
            match self.status:
                
                case "shooting": #disparando proyectiles
                    self.image = self.attack_sprite_left[0]
                
                case "damaged": #recibiendo daño
                    self.image = self.damage_sprite_left[0]
                    
                case "walking": #caminando
                    self.current_sprites = self.walking_sprites_left
                    self.current_sprite += 0.2 / 0.016 * dt

                    if self.current_sprite >= len(self.current_sprites):
                        self.current_sprite = 0
                
                    self.image = self.current_sprites[int(self.current_sprite)]

                case "jumping": #saltando
                    self.current_sprites = self.jumping_sprites_left
                    self.current_sprite += 0.15 / 0.016 * dt

                    if self.current_sprite >= len(self.current_sprites):
                        self.current_sprite = 0
                    
                    self.image = self.current_sprites[int(self.current_sprite)]
        
                case "idle": #estando
                    self.image = self.idle_sprite_left[0]  
            
        #Mirando a la derecha
        elif self.facing == "right":
            match self.status:
                
                case "walking": #caminando
                    self.current_sprites = self.walking_sprites_right
                    self.current_sprite += 0.2 / 0.016 * dt

                    if self.current_sprite >= len(self.current_sprites):
                        self.current_sprite = 0
                
                    self.image = self.current_sprites[int(self.current_sprite)]

                case "jumping": #saltando
                    self.current_sprites = self.jumping_sprites_right
                    self.current_sprite += 0.15 / 0.016 * dt

                    if self.current_sprite >= len(self.current_sprites):
                        self.current_sprite = 0
                    
                    self.image = self.current_sprites[int(self.current_sprite)]
        
                case "idle": #estando
                    self.image = self.idle_sprite_right[0]  
                
                case "damaged": #recibiendo daño
                    self.image = self.damage_sprite_right[0]
                    
                case "shooting": #atacando
                    self.image = self.attack_sprite_right[0]
    
    def shoot(self) -> None:
        """Dispara un proyectil que emite daño."""
        
        if self.projectile_timer <= 0:
            x = self.rect.centerx - 64 if self.facing == "left" else self.rect.centerx
            y = self.rect.centery - 32
            
            pygame.mixer.Sound.play(projectile_sound)
            projectile = Projectile(x, y, self.facing)
            self.projectiles.append(projectile)
            
            self.projectile_timer = self.projectile_cooldown
            self.status = "shooting"
            self.shooting_frame_timer = self.shooting_frame_duration
    
    def update_projectiles(self, dt:float) -> None:
        """Maneja los proyectiles y los mantiene actualizados."""
        
        for projectile in self.projectiles[:]:
            projectile.move(dt)
            if projectile.is_out_of_bounds():
                self.projectiles.remove(projectile)
    
    def draw_projectiles(self, screen:pygame.Surface) -> None:
        """Dibuja los proyectiles en pantalla."""
        
        for projectile in self.projectiles:
            projectile.draw(screen)
    
    def get_hit(self, side:Literal["left", "right"]) -> None:
        """Función para recibir daño; hace funcionar el empuje, reduce la vida y reproduce el sonido de daño."""
        
        pygame.mixer.Sound.play(damage_sound)
        
        self.status = "damaged"
        self.damage_frame_timer = self.damage_frame_duration
        
        if side == "left":
            self.dx += -self.kb_factor * (self.character["health"] - self.hp)
            
        elif side == "right":
            self.dx += self.kb_factor * (self.character["health"] - self.hp)
            
        self.dy = -self.kb_factor * ((self.character["health"] - self.hp) / 10)


    def draw_hitboxes(self, screen:pygame.Surface) -> None:
        """Dibuja la hitbox o caja de colisiones del jugador."""
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        
        
    def update(self, platforms:list, dt:float) -> None:
        """Actualiza la posición del jugador, y hace funcionar las colisiones."""
        
        #Actualizar la posición usando dx para movimiento horizontal y dy para movimiento vertical, la gravedad y la velodad terminal también son factores
        if self.on_ground:
            self.apply_jump_buffer()
            self.jumping = False
            self.double_jump_used = False
            
        self.dy = min(self.terminal_velocity, self.dy + self.gravity)
        
        self.rect.x += self.dx * dt
        self.rect.y += self.dy * dt
        
        #Manejo de colisiones
        self.on_ground = False
        
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.dy > 0:
                    self.dy = 0
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
        
        #Actualizar los proyectiles
        self.update_projectiles(dt)
        
        if self.projectile_timer > 0:
            self.projectile_timer -= dt / 0.016
        
        #Comprobar qué acción está realizando el jugador
        if self.status != "damaged" and self.status != "shooting":
            if self.jumping:
                self.status = "jumping"
            else:
                if self.dx != 0:
                    self.status = "walking"
                else:
                    self.status = "idle"
    
        #Animar al jugador
        self.animate(dt)