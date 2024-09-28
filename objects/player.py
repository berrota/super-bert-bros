import math
import pygame
import time

from typing import Literal

from objects.projectile import Projectile

from misc.characters import *
from misc.files import *

pygame.init()

class Player(pygame.sprite.Sprite):
    """Objeto para el jugador y sus atributos. Aquí se maneja la mayoría de la lógica del movimiento y otras mecánicas del jugador."""
    
    
    ###################################### ATRIBUTOS Y OTROS ######################################
    
    def __init__(self, x: int, y: int, character: dict, name: str, color: str):
        super().__init__()

        #Nombre y color asignados
        self.name: str = name
        self.color = color
        
        #Velocidad / impulso
        self.dx: float = 0
        self.dy: float = 0
        
        #Salto
        self.jumping: bool = False
        self.on_ground: bool = False
        self.double_jump_used = False
        self.jump_buffer_time: float = 0
        self.jump_buffer_duration: float = 0.1
        
        #Invulnerabilidad
        self.invulnerable: bool = False
        self.invulnerability_timer: float = 0

        #Opacidad (para el efecto de pulsación de transparencia al ser invulnerable)
        self.respawn_invincibility: bool = False
        self.opacity: int = 255
        self.pulse_timer: float = 0
                
        #Ataques cuerpo a cuerpo
        self.attacking: bool = False
        self.attack_cooldown: int = 20
        self.attack_timer: float = 0
        self.attack_rect: pygame.Rect = None
        self.hit_registered: bool = False
        
        #Ataques a distancia / proyectiles
        self.projectiles: list[Projectile] = []
        self.projectile_cooldown: int = 25
        self.projectile_timer: float = 0
        
        #Stats. Los valores se dividen por 0.016 porque estaban pensados inicialmente para 60 FPS, y con la adición del delta time los valores se vuelven inconsistentes
        self.character: dict = character
        
        self.lives: int = 2 #Son vidas restantes, no confundir con vidas totales (en total serían 3)
        
        self.velocity: float = character["velocity"] / 0.016
        self.jump_velocity: float = character["jump_velocity"] / 0.016
        self.terminal_velocity: float = character["terminal_velocity"] / 0.016
        self.gravity: float = character["gravity"] / 0.016
        self.kb_factor: float = (character["weight"] ** -1) / 0.016
        
        self.hp: int = character["health"]
        self.damage: int = character["damage"]
        self.projectile_damage: int = character["projectile_damage"]
        self.crit_chance: float = character["crit_chance"]

        #Animaciones, sprites y demás
        self.status: Literal["idle", "damaged", "shooting", "attacking", "walking", "jumping"] = "idle"
        self.facing: Literal["left", "right"] = "right"
        
        self.icon: pygame.Surface = character["icon"]
        
        self.walking_sprites_left: list = character["walking_sprites_left"]
        self.walking_sprites_right: list = character["walking_sprites_right"]
        
        self.jumping_sprites_left: list = character["jumping_sprites_left"]
        self.jumping_sprites_right: list = character["jumping_sprites_right"]
        
        self.idle_sprite_left: list = character["idle_sprite_left"]
        self.idle_sprite_right: list = character["idle_sprite_right"]
        
        self.attack_sprites_left: list = character["attack_sprites_left"]
        self.attack_sprites_right: list = character["attack_sprites_right"]
        
        self.shoot_sprite_left: list = character["shoot_sprite_left"]
        self.shoot_sprite_right: list = character["shoot_sprite_right"]
        self.shoot_frame_duration: int = 15
        self.shoot_frame_timer: float = 0
        
        self.damage_sprite_left: list = character["damage_sprite_left"]
        self.damage_sprite_right: list = character["damage_sprite_right"]
        self.damage_frame_duration: int = 8
        self.damage_frame_timer: float = 0
        
        self.current_sprites: list = self.idle_sprite_right
        self.current_sprite: float = 0
        self.image: pygame.Surface = self.current_sprites[self.current_sprite]

        #Hitbox
        self.rect: pygame.Rect = pygame.Rect(x, y, self.idle_sprite_left[0].get_width(), self.idle_sprite_left[0].get_height())
        self.rect.topleft = [x, y]
    
    
    ###################################### MOVIMIENTO ######################################
    
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
            
            
    ###################################### ATAQUES Y RECEPCIÓN DE DAÑO ######################################
    
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
            self.shoot_frame_timer = self.shoot_frame_duration
    
    def update_projectiles(self, dt: float) -> None:
        """Maneja los proyectiles y los mantiene actualizados."""
        
        for projectile in self.projectiles[:]:
            projectile.move(dt)
            if projectile.is_out_of_bounds():
                self.projectiles.remove(projectile)
    
    def draw_projectiles(self, screen:pygame.Surface) -> None:
        """Dibuja los proyectiles en pantalla."""
        
        for projectile in self.projectiles:
            projectile.draw(screen)
    
    
    def attack(self) -> None:
        """Activa un ataque cuerpo a cuerpo si el cooldown lo permite."""
        if self.attack_timer <= 0:
            self.attacking = True
            self.attack_timer = self.attack_cooldown
            self.hit_registered = False
            self.status = "attacking"
    
    def create_attack_hitbox(self) -> pygame.Rect:
        """Crea una hitbox o caja de colisiones para el ataque cuerpo a cuerpo."""
        if self.facing == "left":
            attack_rect = pygame.Rect(self.rect.left - 50,  self.rect.top, 50, self.rect.height)
        else:
            attack_rect = pygame.Rect(self.rect.right, self.rect.top, 50, self.rect.height)
        
        return attack_rect
    
    def check_attack_collisions(self, player) -> None:
        """Comprobar si la hitbox del ataque melee ha colisionado con un jugador. Si sí, golpearlo."""
        self.attack_rect = self.create_attack_hitbox()
        
        if self.attack_rect.colliderect(player.rect) and not self.hit_registered:
            self.hit_registered = True
            pygame.mixer.Sound.play(attack_sound)
            self.attack_rect = None
            player.get_hit("left" if player.rect.center < self.rect.center else "right", self.damage)
    
    def update_attack(self, dt: float, player) -> None:
        """Actualizar el estado del ataque y su temporizador."""
        if self.attacking:
            self.check_attack_collisions(player)
        
        if self.attack_timer > 0:
            self.attack_timer -= dt / 0.016
            
            if self.attacking:
                self.status = "attacking"
                
            if self.attack_timer <= 0:
                self.attacking = False
                self.attack_rect = None
                self.status = "idle"
        
        if not self.attacking:
            self.attack_rect = None
    
    def take_damage(self, amount: int):
        """Resta la cantidad de daño especificada a la vida del jugador si no es invulnerable."""
        if not self.invulnerable:
            #Reducir vida
            self.hp -= amount
            
            #Invulnerabilidad por 300 ms
            self.gain_invulnerability(300, milliseconds=True)
            
            #Resetear invincibilidad de reaparición al recibir daño
            self.respawn_invincibility = False
    
    def get_hit(self, side:Literal["left", "right"], amount: int) -> None:
        """Función para recibir daño; hace funcionar el empuje, reduce la vida y reproduce el sonido de daño."""
        
        if self.invulnerable:
            return
        
        pygame.mixer.Sound.play(damage_sound)
        
        self.status = "damaged"
        self.damage_frame_timer = self.damage_frame_duration
        
        self.take_damage(amount)
        
        self.dy = -self.kb_factor * ((self.character["health"] - self.hp) / 10)
        
        if side == "left":
            self.dx += -self.kb_factor * (self.character["health"] - self.hp)
            
        elif side == "right":
            self.dx += self.kb_factor * (self.character["health"] - self.hp)
    
    
    def gain_invulnerability(self, time: float, milliseconds: bool = False, respawn: bool = False) -> None:
        """Concede invulnerabilidad al jugador por el lapso de tiempo deseado."""
        if milliseconds: #Conversión a milisegundos
            time /= 1000
        
        self.invulnerable = True
        self.invulnerability_timer = time
        
        #Conceder invincibilidad de reaparición
        self.respawn_invincibility = respawn
    
        
    ###################################### ACTUALIZACIÓN Y ANIMACIONES ######################################

    def animate(self, dt: float) -> None:
        """Animaciones."""
        #Temporizador de la duración de la animación de disparo
        if self.shoot_frame_timer > 0:
            self.status = "shooting"
            self.shoot_frame_timer -= dt / 0.016
        else:
            if self.status == "shooting":
                self.status = "idle"
        
        #Recibiendo daño
        if self.damage_frame_timer > 0:
            self.status = "damaged"
            self.damage_frame_timer -= dt / 0.016 
        else:
            if self.status == "damaged":
                self.status = "idle"
                
        #Atacando
        if self.attacking:
            self.status = "attacking"
        
        #Mirando a la izquierda
        if self.facing == "left":
            match self.status:
                
                case "idle": #estando
                    self.image = self.idle_sprite_left[0]  
                
                case "damaged": #recibiendo daño
                    self.image = self.damage_sprite_left[0]
                    
                case "shooting": #disparando un proyectil
                    self.image = self.shoot_sprite_left[0]
                
                case "attacking": #ataque cuerpo a cuerpo
                    self.current_sprites = self.attack_sprites_left
                    self.current_sprite += 0.2 / 0.016 * dt
                    
                    if self.current_sprite >= len(self.current_sprites):
                        self.current_sprite = 0
                        
                    self.image = self.current_sprites[int(self.current_sprite)]
                    
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
        
            
        #Mirando a la derecha
        elif self.facing == "right":
            match self.status:
                
                case "idle": #estando
                    self.image = self.idle_sprite_right[0]  
                    
                case "damaged": #recibiendo daño
                    self.image = self.damage_sprite_right[0]
                    
                case "shooting": #disparando un proyectil
                    self.image = self.shoot_sprite_right[0]
                
                case "attacking": #ataque cuerpo a cuerpo
                    self.current_sprites = self.attack_sprites_right
                    self.current_sprite += 0.2 / 0.016 * dt
                    
                    if self.current_sprite >= len(self.current_sprites):
                        self.current_sprite = 0
                        
                    self.image = self.current_sprites[int(self.current_sprite)]
                    
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
        
        
    def draw_hitboxes(self, screen:pygame.Surface) -> None:
        """Dibuja la hitbox o caja de colisiones del jugador."""
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        if self.attack_rect:
            pygame.draw.rect(screen, (0, 255, 0), self.attack_rect, 2)
    
        
    def update(self, platforms: list, dt: float) -> None:
        """Actualiza la posición del jugador, y hace funcionar las colisiones."""
        
        #Comprobar si el jugador se encuentra en el suelo, y si lo está resetear el salto doble y aplicar el buffering del salto
        if self.on_ground:
            self.apply_jump_buffer()
            self.jumping = False
            self.double_jump_used = False
        
        #Aplicar gravedad y asegurarse de que la velocidad del jugador no exceda la velocidad terminal
        self.dy = min(self.terminal_velocity, self.dy + self.gravity)
        
        #Aplicar velocidad a la posición del jugador
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
        #los ataques cuerpo a cuerpo se actualizan en game.py
        self.update_projectiles(dt)
        
        if self.projectile_timer > 0:
            self.projectile_timer -= dt / 0.016
        
        #Temporizador de invulnerabilidad
        if self.invulnerable:
            self.invulnerability_timer -= dt
            if self.invulnerability_timer <= 0:
                self.invulnerable = False
                self.invulnerability_timer = 0
        
        #Efecto de pulsación
        if self.invulnerable and self.respawn_invincibility:
            self.pulse_timer += dt
            self.opacity = int((math.sin(self.pulse_timer * 3) + 1) * 127.5)  # Pulsing effect
        else:
            self.opacity = 255
        
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
    
    def draw(self, screen:pygame.Surface) -> None:
        """Método personalizado para dibujar al jugador en pantalla, con su atributo de opacidad."""
        image = self.image.copy()
        image.set_alpha(self.opacity if self.opacity > 25 else 25) #no hacerlo completamente transparente
        screen.blit(image, self.rect)