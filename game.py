from objects.platform import Platform
from objects.player import Player
from objects.projectile import Projectile

from screen.character_selection import character_selection_screen
from screen.pause import draw_pause_screen
from screen.volume import change_volume

from misc.characters import *
from misc.colors import *
from misc.files import *
from misc.key_bindings import *

import pygame
import random 
import sys

from tkinter import messagebox


def main():
    
    #Inicializar cosas generales
    pygame.init()
    
    FPS = 60
    clock = pygame.time.Clock()
    
    hitbox = False
    pause = False

    #Proyectiles
    max_projectiles = 8
    player1_projectiles = []
    player2_projectiles = []
    projectile_cooldown = 25 #En ticks (60 ticks por segundo)
    player1_projectile_cooldown = 0
    player2_projectile_cooldown = 0

    #Pantalla
    screen_width = 1920
    screen_height = 1080
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    pygame.display.set_caption("super bert bros (please don't sue me nintendo)")
    pygame.display.set_icon(pygame.image.load("assets/images/icon.png"))

    #Superficie
    surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

    #Volumen inicial
    volume = 1
    music_volume = 1

    #Dejar que el jugador seleccione los personajes deseados
    characters = character_selection_screen("Player 1", "random", "Player 2", "random")

    #Crear grupos de sprites y los jugadores
    players = pygame.sprite.Group()
    
    player1 = Player(640, 0, characters[0], characters[2])
    player2 = Player(1080, 0, characters[1], characters[3])

    players.add(player1, player2)
    
    #Crear las plataformas
    platforms = (
        Platform(360, 500, 1200, 300, "big"),
        Platform(640, 250, 200, 30, "small"),
        Platform(1080, 250, 200, 30, "small")
    )

    #Reproducir música
    pygame.mixer.music.load("assets/sound/music.mp3")
    pygame.mixer.music.set_volume(0.07)
    pygame.mixer.music.play(0)

    #Bucle del juego (lo que pasa cada tick - 60 veces por segundo)
    while True:

        #Si el juego está pausado, dibujar el menú de pausa y pausar la música
        if pause:
            pygame.mixer.music.pause()
            resume, quit, change_characters, change_volume_button = draw_pause_screen(surface, screen_width, screen_height)

        #Manejo de eventos
        for event in pygame.event.get():

            if event.type == pygame.QUIT: #Cerrar el juego
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN: #pulsación de teclas
                if event.key == K_pause: #pausa
                    pause = not pause
                    
                elif event.key == K_hitbox: #dibujar hitboxes
                    hitbox = not hitbox
                    
                elif event.key == K_player1_jump and not pause: #salto de jugador 1
                    player1.jump(platforms)
                    
                elif event.key == K_player2_jump and not pause: #salto de jugador 2
                    player2.jump(platforms)
                    
                elif event.key == K_player1_projectile and not pause and player1_projectile_cooldown <= 0: #proyectiles de jugador 1
                    pygame.mixer.Sound.play(projectile_sound)
                    
                    if player1.facing == "left":
                        projectile_x = player1.rect.x - 20
                        
                    elif player1.facing == "right":
                        projectile_x = player1.rect.x + 20
                        
                    player1_projectile_cooldown = projectile_cooldown
                    player1_projectiles.append(Projectile(projectile_x, player1.rect.y, player1.facing, players))
                    
                elif event.key == K_player2_projectile and not pause and player2_projectile_cooldown <= 0: # proyectiles de jugador 2
                    pygame.mixer.Sound.play(projectile_sound)
                    
                    if player2.facing == "left":
                        projectile_x = player2.rect.x - 20
                        
                    elif player2.facing == "right":
                        projectile_x = player2.rect.x + 20
                        
                    player2_projectile_cooldown = projectile_cooldown
                    player2_projectiles.append(Projectile(projectile_x, player2.rect.y, player2.facing, players))
                    
                elif event.key == K_quit: #cerrar el juego por medio de la pulsación de la tecla de cerrado
                    pygame.quit()
                    sys.exit()
            

            #Hacer que los botones del menú de pausa funcionen
            elif event.type == pygame.MOUSEBUTTONDOWN and pause:

                #Cerrar menú de pausa y continuar la partida
                if resume.collidepoint(event.pos):
                    pause = False
                
                #Cerrar juego
                if quit.collidepoint(event.pos):
                    pygame.quit
                    sys.exit()
                
                #Cambiar personajes
                if change_characters.collidepoint(event.pos):
                    characters = character_selection_screen(player1.name, player1.character["name"], player2.name, player2.character["name"])
                    player1.__init__(player1.rect.x, player1.rect.y, characters[0], characters[2])
                    player2.__init__(player2.rect.x, player2.rect.y, characters[1], characters[3])
                
                #Ajustar volumen
                if change_volume_button.collidepoint(event.pos):
                    volumes = change_volume(volume, music_volume)
                    current_volume = volumes[0]
                    current_music_volume = volumes[1]
                    death_sound.set_volume(death_sound.get_volume() * current_volume)
                    projectile_sound.set_volume(death_sound.get_volume() * current_volume)
                    void_death_sound.set_volume(death_sound.get_volume() * current_volume)
                    damage_sound.set_volume(death_sound.get_volume() * current_volume)
                    game_end_sound.set_volume(death_sound.get_volume() * current_volume)
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() * current_music_volume)
                    volume = current_volume
                    music_volume = current_music_volume
        
        #Si el juego NO está pausado, actualizar como de costumbre
        if not pause:
            
            #Si la música está pausada, continuar reproduciéndola
            if pygame.mixer.music.get_busy:
                pygame.mixer.music.unpause()

            #Manejo de teclas
            keys = pygame.key.get_pressed()
                
            #Jugador 1
            if keys[K_player1_left] and keys[K_player1_right]:
                player1.move(0)
                
            elif keys[K_player1_left]:
                player1.move(-1)
                
            elif keys[K_player1_right]:
                player1.move(1)
                
            else:
                player1.move(0)
            
            if keys[K_player1_projectile]:
                player1.status = "attacking"

            #Jugador 2
            if keys[K_player2_left] and keys[K_player2_right]:
                player2.move(0)
            elif keys[K_player2_left]:
                player2.move(-1)
            elif keys[K_player2_right]:
                player2.move(1)
            else:
                player2.move(0)
            
            if keys[K_player2_projectile]:
                player2.status = "attacking"


            #Proyectiles de jugador 1
            for projectile in player1_projectiles:

                #Eliminar los proyectiles
                if projectile.rect.x >= screen_width or projectile.rect.x <= 0:
                    player1_projectiles.remove(projectile)

                #Hacer que haga daño
                if projectile.rect.colliderect(player2.rect):
                    player2.get_hit(projectile.direction)
                    player1_projectiles.remove(projectile)
                    player2.hp -= player1.projectile_damage

            #Proyectiles de jugador 2
            for projectile in player2_projectiles:

                #Eliminar los proyectiles
                if projectile.rect.x >= screen_width or projectile.rect.x <= 0:
                    player2_projectiles.remove(projectile)

                #Hacer que haga daño
                if projectile.rect.colliderect(player1.rect):
                    player1.get_hit(projectile.direction)
                    player2_projectiles.remove(projectile)
                    player1.hp -= player2.projectile_damage
            
            if len(player1_projectiles) > max_projectiles: #Máximos proyectiles
                player1_projectiles.pop(0)

            if len(player2_projectiles) > max_projectiles: #Máximos proyectiles
                player2_projectiles.pop(0)

            #Actualizar jugadores
            players.update(platforms) 

            #Vidas y muerte
            for player in players:
                
                if player.rect.y >= screen_height + 100:
                    if player.lives > 0:
                            pygame.mixer.Sound.play(void_death_sound)
                            player.hp = player.character["health"]
                            player.rect.x = random.choice([640, 1080])
                            player.rect.y = -2000
                            player.lives -= 1
                    elif player.lives == 0:
                        pygame.mixer.Sound.play(game_end_sound)
                        player.lives -= 1
                        
                if player.hp <= 0:
                    if player.lives > 0:
                        pygame.mixer.Sound.play(death_sound)
                        player.hp = player.character["health"]
                        player.rect.x = random.choice([640, 1080])
                        player.rect.y = -2000
                        player.lives -= 1
                    elif player.lives == 0:
                        player.lives -= 1
        
            player1_projectile_cooldown -= 1
            player2_projectile_cooldown -= 1


            if player1.lives == -1 and player2.lives == -1:
                pygame.mixer.Sound.play(game_end_sound)
                messagebox.showinfo("AMBOS CHABALES HAN MORIDO", "pringaos")
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()
            elif player1.lives == -1:
                pygame.mixer.Sound.play(game_end_sound)
                messagebox.showinfo("GGs", f"1º: {player2.name} ({player2.character["name"]}) \n2º: {player1.name} ({player1.character["name"]}) \n\nClica OK para cerrar el juego.")
                pygame.quit()
                sys.exit()
            elif player2.lives == -1:
                pygame.mixer.Sound.play(game_end_sound)
                messagebox.showinfo("GGs", f"1º: {player1.name} ({player1.character["name"]}) \n2º: {player2.name} ({player2.character["name"]}) \n\nClica OK para cerrar el juego.")
                pygame.quit()
                sys.exit()
        
                
        """Dibujar todo en pantalla."""
        
        #Fondo
        screen.blit(bg_image, (0, 0))

        #Icono de jugador 1
        screen.blit(player1.icon, (480, 840))
        
        #Nombre de jugador 1
        pygame.draw.rect(screen, WHITE, (480, 950, 150, 45), 0, 8)
        screen.blit(font.render(f"{player1.name}", True, BLACK), (490, 955))
        
        #Vida de jugador 1
        if player1.lives >= 0:
            screen.blit(title_font.render(f"{str(player1.hp)} hp", True, WHITE), (480, 900))
            
            #Vidas de jugador 1
            if player1.lives == 2:
                screen.blit(heart_image, (550, 997))
                screen.blit(heart_image, (515, 997))
                screen.blit(heart_image, (480, 997))
                
            elif player1.lives == 1:
                screen.blit(heart_image, (515, 997))
                screen.blit(heart_image, (480, 997))
                
            elif player1.lives == 0:
                screen.blit(heart_image, (480, 997))
                
        elif player1.lives < 0:
            screen.blit(title_font.render("MUERTO", True, DARK_RED), (480, 900))


        #Icono de jugador 2
        screen.blit(player2.icon, (1315, 840))
        
        #Nombre de jugador 2
        pygame.draw.rect(screen, WHITE, (1315, 950, 150, 45), 0, 8)
        screen.blit(font.render(f"{player2.name}", True, BLACK), (1325, 955))
        
        #Vida de jugador 2
        if player2.lives >= 0:
            screen.blit(title_font.render(f"{str(player2.hp)} hp", True, WHITE), (1315, 900))
            
            #Vidas de jugador 2
            if player2.lives == 2:
                screen.blit(heart_image, (1385, 997))
                screen.blit(heart_image, (1350, 997))
                screen.blit(heart_image, (1315, 997))
                
            elif player2.lives == 1:
                screen.blit(heart_image, (1350, 997))
                screen.blit(heart_image, (1315, 997))
                
            elif player2.lives == 0:
                screen.blit(heart_image, (1315, 997))
                
        elif player2.lives < 0:
            screen.blit(title_font.render("MUERTO", True, DARK_RED), (1315, 900))
    
        #Plataformas
        for platform in platforms:
            platform.draw(screen)
        
        #Jugadores
        players.draw(screen)

        #Proyectiles
        for projectile in player1_projectiles:
            projectile.draw(screen)
        
        for projectile in player2_projectiles:
            projectile.draw(screen)
        
        #Hitboxes (si están activadas)
        if hitbox == True:
            for platform in platforms:
                platform.draw_hitboxes(screen)

            for player in players:
                player.draw_hitboxes(screen)

            for projectile in player1_projectiles:
                projectile.draw_hitboxes(screen)

            for projectile in player2_projectiles:
                projectile.draw_hitboxes(screen)

        #Superficie gris semi-transparente
        if pause:
            screen.blit(surface, (0, 0))

        #Actualizar juego a 60 FPS
        pygame.display.update()
        dt = clock.tick(FPS) / 1000