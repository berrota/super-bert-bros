import json
import pygame
import random
import pygetwindow
import sys
import time

from tkinter import messagebox
from typing import NoReturn

from objects.platform import Platform
from objects.player import Player

from screen.character_selection import character_selection_screen
from screen.settings import settings_screen
from screen.pause import draw_pause_screen
from screen.volume import change_volume_screen

from misc.characters import *
from misc.colors import *
from misc.files import *

from preferences.key_bindings import *

from util.translator import translate

def main() -> NoReturn:
    """Función que contiene el \"core\" del juego."""
    
    #Importar ajustes
    with open("preferences/options.json", "r") as options_file:
        preferences = json.load(options_file)
    
    VSYNC = preferences["vsync"]
    LANG = preferences["lang"]
    
    with open("preferences/volume.json", "r") as volume_file:
        volume_preferences = json.load(volume_file)
    
    SFX = volume_preferences["sfx"]
    MUSIC = volume_preferences["music"]
    
    #Inicializar cosas generales
    pygame.init()
    
    FPS: int = 60
    clock: pygame.time.Clock = pygame.time.Clock()
    prev_time: float = time.time()
    deltaTime: float = 0
    
    debug: bool = False
    pause: bool = False

    #Proyectiles
    MAX_PROJECTILES: int = 8

    #Pantalla
    SCREEN_WIDTH: int = 1920
    SCREEN_HEIGHT: int = 1080
    
    fullscreen: bool = True
    
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pygame.display.set_caption(translate("title"))
    pygame.display.set_icon(pygame.image.load("assets/images/icon.png"))

    #Superficie para poder utilizar transparencia
    surface: pygame.Surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    
    #Dejar que el jugador seleccione los personajes deseados
    characters: tuple = character_selection_screen( #Formato: nombre por defecto, personaje por defecto, color por defecto
        translate("player1.name"), "random", "#FF0000", 
        translate("player2.name"), "random", "#0000FF"
    )

    #Crear grupos de sprites y los jugadores
    players: pygame.sprite.Group = pygame.sprite.Group()
    
    player1: Player = Player(640, 0, characters[0], characters[2], characters[4])
    player2: Player = Player(1080, 0, characters[1], characters[3], characters[5])

    players.add(player1, player2)
    
    #Crear las plataformas
    platforms: tuple = (
        Platform(360, 500, 1200, 300, "big"),
        Platform(640, 250, 200, 30, "small"),
        Platform(1080, 250, 200, 30, "small")
    )
    
    #Ajustar volumen desde preferencias guardadas
    sfx_volume = SFX
    music_volume = MUSIC
    
    def change_volumes(sfx: float = 1, music: float = 1) -> None:
        """Ajusta el volumen de los efectos sonoros y de la música."""
        pygame.mixer.music.set_volume(0.07 * music)
        
        death_sound.set_volume(0.9 * sfx)
        attack_sound.set_volume(0.7 * sfx)
        projectile_sound.set_volume(0.2 * sfx)
        void_death_sound.set_volume(0.07 * sfx)
        damage_sound.set_volume(0.8 * sfx)
        game_end_sound.set_volume(0.1 * sfx)
    
    change_volumes(SFX, MUSIC)
    
    #Reproducir música
    pygame.mixer.music.play(-1) #hacer que la música entre en bucle, especificándole -1 ciclos

    #Bucle del juego (lo que pasa cada tick)
    while True:
        
        #Delta time (actualizar de manera constante independientemente de los FPS)
        now = time.time()
        deltaTime = (now - prev_time)
        prev_time = now

        #Si el juego está pausado, dibujar el menú de pausa y pausar la música
        if pause:
            pygame.mixer.music.pause()
            resume, quit, change_characters, change_volume_button, options = draw_pause_screen(surface, SCREEN_WIDTH, SCREEN_HEIGHT)

        #Manejo de eventos
        for event in pygame.event.get():

            if event.type == pygame.QUIT: #Cerrar el juego
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN: #pulsación de teclas
                if event.key == K_pause: #pausa
                    pause = not pause
                    if not pause:
                        pygame.mixer.unpause() #no funciona pero bueno
                                    
                elif event.key == K_fullscreen: #pantalla completa
                    fullscreen = not fullscreen
                    if fullscreen:
                        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN, vsync=VSYNC)
                        try:
                            window = pygetwindow.getWindowsWithTitle(translate("title"))[0]
                            window.moveTo(0, 0)
                        except IndexError:
                            pass
                    else:
                        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync=VSYNC)
                        try:
                            window = pygetwindow.getWindowsWithTitle(translate("title"))[0]
                            window.moveTo(100, 100)
                        except IndexError:
                            pass
                    
                elif event.key == K_debug: #dibujar información de debug
                    debug = not debug
                    
                elif event.key == K_player1_jump and not pause: #salto de jugador 1
                    player1.jump()
                    
                elif event.key == K_player2_jump and not pause: #salto de jugador 2
                    player2.jump()
                    
                elif event.key == K_player1_projectile and not pause: #proyectiles de jugador 1
                    player1.shoot()
                    
                elif event.key == K_player2_projectile and not pause: # proyectiles de jugador 2
                    player2.shoot()
                
                elif event.key == K_player1_attack and not pause: #ataques cuerpo a cuerpo de jugador 1
                    player1.attack()
                
                elif event.key == K_player2_attack and not pause: #ataques cuerpo a cuerpo de jugador 2
                    player2.attack()
                    
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
                    pygame.quit()
                    sys.exit()
                
                #Cambiar personajes
                if change_characters.collidepoint(event.pos):
                    #Almacenar vida y puntos de vida totales anteriores de los jugadores
                    old_player1_hp = player1.__getattribute__("hp")
                    old_player1_total_hp = player1.__getattribute__("character")["health"]
                    
                    old_player2_hp = player2.__getattribute__("hp")
                    old_player2_total_hp = player2.__getattribute__("character")["health"]
                    
                    #Dejar a los jugadores elegir sus nuevos personajes
                    characters = character_selection_screen(player1.name, player1.character["name"], player1.color, player2.name, player2.character["name"], player2.color)
                    
                    #Cambiar personajes, nombres y colores a los deseados
                    player1.__init__(player1.rect.x, player1.rect.y, characters[0], characters[2], characters[4])
                    player2.__init__(player2.rect.x, player2.rect.y, characters[1], characters[3], characters[5])
                    
                    #Multiplicar nueva vida total por la relatividad de la vida y vida total anteriores al cambio
                    new_player1_hp = (old_player1_hp / old_player1_total_hp) * player1.hp
                    new_player2_hp = (old_player2_hp / old_player2_total_hp) * player2.hp
                    
                    #Convertir a números enteros para evitar errores con la vida
                    player1.hp = int(new_player1_hp)
                    player2.hp = int(new_player2_hp)
                
                #Ajustar volumen
                if change_volume_button.collidepoint(event.pos):
                    volumes = change_volume_screen(sfx_volume, music_volume)
                    sfx_volume = volumes[0]
                    music_volume = volumes[1]
                    change_volumes(sfx_volume, music_volume)
                
                #Ajustes / configuración
                if options.collidepoint(event.pos):
                    VSYNC, fullscreen, LANG = settings_screen()
                    
                    if fullscreen:
                        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN, vsync=VSYNC)
                        try:
                            window = pygetwindow.getWindowsWithTitle(translate("title"))[0]
                            window.moveTo(0, 0)
                        except IndexError:
                            pass
                    else:
                        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync=VSYNC)
                        try:
                            window = pygetwindow.getWindowsWithTitle(translate("title"))[0]
                            window.moveTo(100, 100)
                        except IndexError:
                            pass
        
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

            #Jugador 2
            if keys[K_player2_left] and keys[K_player2_right]:
                player2.move(0)
                
            elif keys[K_player2_left]:
                player2.move(-1)
                
            elif keys[K_player2_right]:
                player2.move(1)
                
            else:
                player2.move(0)

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
            
            #Actualizar ataques cuerpo a cuerpo
            for player in players:
                player.update_attack(deltaTime, player2 if player == player1 else player1)
            
            #Actualizar jugadores
            players.update(platforms, deltaTime) 

            #Vidas y muerte
            for player in players:
                
                if player.rect.y >= SCREEN_HEIGHT + 100:
                    if player.lives > 0:
                            pygame.mixer.Sound.play(void_death_sound)
                            player.hp = player.character["health"]
                            player.gain_invulnerability(5, respawn=True)
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
                        player.gain_invulnerability(5, respawn=True)
                        player.rect.x = random.choice([640, 1080])
                        player.rect.y = -2000
                        player.lives -= 1
                    elif player.lives == 0:
                        player.lives -= 1
        
            if player1.lives == -1 and player2.lives == -1:
                pygame.mixer.Sound.play(game_end_sound)
                messagebox.showinfo(translate("tie.title"), translate("tie.text"))
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()
                
            elif player1.lives == -1:
                message = (
                    f"{translate("first")}: {player2.name} {translate("using")} {player2.character["name"]} \n"
                    f"{translate("second")}: {player1.name} {translate("using")} {player1.character["name"]} \n\n"
                    f"{translate("ok.text")}"
                )
                
                pygame.mixer.Sound.play(game_end_sound)
                messagebox.showinfo("GGs", message)
                pygame.quit()
                sys.exit()
                
            elif player2.lives == -1:
                message = (
                    f"{translate("first")}: {player1.name} {translate("using")} {player1.character["name"]} \n"
                    f"{translate("second")}: {player2.name} {translate("using")} {player2.character["name"]} \n\n"
                    f"{translate("ok.text")}"
                )
                
                pygame.mixer.Sound.play(game_end_sound)
                messagebox.showinfo("GGs", message)
                pygame.quit()
                sys.exit()
        
                
        """Dibujar todo en pantalla."""
        
        #Fondo
        screen.blit(bg_image, (0, 0))

        #Icono de jugador 1
        screen.blit(player1.icon, (480, 840))
        
        #Nombre de jugador 1
        player1_name_surface = font.render(player1.name, True, player1.color)
        player1_text_width = player1_name_surface.get_width()
        player1_text_width += 20 #añadir padding (espacio a los lados)
        pygame.draw.rect(screen, WHITE, (480, 950, player1_text_width, 45), 0, 8)
        screen.blit(player1_name_surface, (490, 955))
        
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
            screen.blit(title_font.render(translate("dead"), True, DARK_RED), (480, 900))


        #Icono de jugador 2
        screen.blit(player2.icon, (1315, 840))
        
        #Nombre de jugador 2
        player2_name_surface = font.render(player2.name, True, player2.color)
        player2_text_width = player2_name_surface.get_width()
        player2_text_width += 20 #añadir padding (espacio a los lados)
        pygame.draw.rect(screen, WHITE, (1315, 950, player2_text_width, 45), 0, 8)
        screen.blit(player2_name_surface, (1325, 955))
        
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
            screen.blit(title_font.render(translate("dead"), True, DARK_RED), (1315, 900))
    
        #Plataformas
        for platform in platforms:
            platform.draw(screen)
        
        #Jugadores
        for player in players:
            player.draw(screen)
        
        #Proyectiles
        for player in players:
            player.draw_projectiles(screen)
        
        #Etiquetas de nombre para los jugadores
        for player in players:
            player_nametag = small_font.render(player.name, True, hex_to_rgb(player.color))
            player_name_width = player_nametag.get_width() + 20
            player_name_height = 30
            
            player_name_x = player.rect.x + (player.rect.width // 2) - (player_name_width // 2)
            player_name_y = player.rect.y - player_name_height - 10
            
            pygame.draw.rect(screen, WHITE, (player_name_x, player_name_y, player_name_width, player_name_height), 0, 8)
            screen.blit(player_nametag, (player_name_x + 10, player_name_y + 2))

        #Hitboxes y otra información debug (si están activadas)
        if debug:
            for platform in platforms:
                platform.draw_hitboxes(screen)

            for player in players:
                player.draw_hitboxes(screen)

            for projectile in player1.projectiles:
                projectile.draw_hitboxes(screen)

            for projectile in player2.projectiles:
                projectile.draw_hitboxes(screen)
            
            screen.blit(font.render(f"Player 1 status: {player1.status}", True, BLACK), (0, 0))
            screen.blit(font.render(f"Player 2 status: {player2.status}", True, BLACK), (0, 30))
            screen.blit(font.render(f"Player 1 inv.: {player1.invulnerable} for {int(player1.invulnerability_timer * 1000)} ms", True, BLACK), (0, 60))
            screen.blit(font.render(f"Player 2 inv.: {player2.invulnerable} for {int(player2.invulnerability_timer * 1000)} ms", True, BLACK), (0, 90))

        #Superficie gris semi-transparente
        if pause:
            screen.blit(surface, (0, 0))
            pygame.mixer.pause()
        
        #Actualizar juego
        pygame.display.update()
        clock.tick(FPS) #de momento voy a mantener los FPS fijados a 60 para no romper nada más