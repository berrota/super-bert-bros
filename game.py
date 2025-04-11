import json
import pygame
import pygetwindow
import sys
import time

from typing import NoReturn

from objects.platform import Platform
from objects.player import Player, handle_player_inputs, handle_player_lives
from objects.projectile import handle_projectile_logic

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
    
    clock: pygame.time.Clock = pygame.time.Clock()
    prev_time: float = time.time()
    deltaTime: float = 0
    
    debug: bool = False
    pause: bool = False

    # Pantalla
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
    
    player1: Player = Player(1/3 * SCREEN_WIDTH, 0, characters[0], characters[2], characters[4])
    player2: Player = Player(2/3 * SCREEN_WIDTH, 0, characters[1], characters[3], characters[5])

    players.add(player1, player2)
    
    #Crear las plataformas
    platforms: tuple = (
        Platform(relres(360, 500, 1200, 300), "big"),
        Platform(relres(640, 250, 200, 30), "small"),
        Platform(relres(1080, 250, 200, 30), "small")
    )
    
    #Ajustar volumen desde preferencias guardadas
    sfx_volume = SFX
    music_volume = MUSIC
    
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
        else:
            resume = quit = change_characters = change_volume_button = options = None

        #Manejo de eventos
        for event in pygame.event.get():
            pause, debug, sfx_volume, music_volume = handle_game_events(event, pause, debug, players, resume, quit, change_characters, change_volume_button, options, sfx_volume, music_volume)
        
        #Si el juego NO está pausado, actualizar como de costumbre
        if not pause:
            
            #Si la música está pausada, continuar reproduciéndola
            if pygame.mixer.music.get_busy:
                pygame.mixer.music.unpause()

            #Manejo de teclas
            keys_list = list(pygame.key.get_pressed())
            prev_keys = keys_list.copy()
            keys = pygame.key.ScancodeWrapper(keys_list)

            handle_player_inputs(keys, players, prev_keys, deltaTime)

            #Lógica de proyectiles
            handle_projectile_logic(players, platforms)
            
            #Actualizar ataques cuerpo a cuerpo
            for player in players:
                player.update_attack(deltaTime, player2 if player == player1 else player1)
            
            #Actualizar jugadores
            players.update(platforms, deltaTime) 
            handle_player_lives(players)

        #Dibujar el pantalla todos los objetos
        render(screen, players, platforms, debug)
        
        #Superficie gris semi-transparente
        if pause:
            screen.blit(surface, (0, 0))
            pygame.mixer.pause()
        
        #Actualizar juego
        pygame.display.update()
        clock.tick(FPS) #de momento voy a mantener los FPS fijados a 60 para no romper nada más



def handle_game_events(event: pygame.event.Event, pause: bool, debug: bool, players: pygame.sprite.Group,
                       resume: pygame.Surface, quit: pygame.Surface, change_characters: pygame.Surface, 
                       change_volume_button: pygame.Surface, options: pygame.Surface,
                       sfx_volume: float, music_volume: float) -> tuple[bool, bool, float, float]:
    """Maneja todos los eventos del juego, es decir, las cosas que ocurren, tal y como la pulsación de teclas y cerrado de ventana."""
    player1, player2 = players
    
    #Cerrar el juego si el jugador lanza el evento de cierre por medio de cerrar la ventana o terminar el proceso
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    #Pulsación de teclas (detecta las teclas sólo cuando son pulsadas, pero no si son mantenidas)
    elif event.type == pygame.KEYDOWN:
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
            old_player1_hp = player1.hp
            old_player1_total_hp = player1.character["health"]
            
            old_player2_hp = player2.hp
            old_player2_total_hp = player2.character["health"]
            
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
    
    #Mantener la variable "pause" actualizada, además de los valores de volumen
    return pause, debug, sfx_volume, music_volume

def change_volumes(sfx: float = 1, music: float = 1) -> None:
    """Ajusta el volumen de los efectos sonoros y de la música."""
    pygame.mixer.music.set_volume(0.07 * music)
    
    death_sound.set_volume(0.9 * sfx)
    attack_sound.set_volume(0.7 * sfx)
    projectile_sound.set_volume(0.2 * sfx)
    void_death_sound.set_volume(0.07 * sfx)
    damage_sound.set_volume(0.8 * sfx)
    game_end_sound.set_volume(0.1 * sfx)


def render(screen: pygame.Surface, players: pygame.sprite.Group, platforms: tuple, debug: bool) -> None:
    """Dibuja todos los objetos necesarios en pantalla."""
    player1, player2 = players
    
    # superficie buffer para la resolución relativa
    buffer_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    
    #Fondo
    buffer_surface.blit(bg_image, (0, 0))
    
    # Icono de jugador 1
    if player1.should_render_dead_icon:
        buffer_surface.blit(player1.dead_icon, relres(480, 830))
    else:
        buffer_surface.blit(player1.icon, relres(480, 840))
    
    # Nombre de jugador 1
    player1_name_surface = font.render(player1.name, True, player1.color)
    player1_text_width = player1_name_surface.get_width()
    player1_text_width += relres(20)  # Añadir padding (espacio a los lados)
    pygame.draw.rect(buffer_surface, WHITE, relres(480, 950, player1_text_width / SCREEN_WIDTH * 1920, 45), 0, 8)
    buffer_surface.blit(player1_name_surface, relres(490, 955))
    
    # Vida de jugador 1
    if player1.lives >= 0:
        buffer_surface.blit(title_font.render(f"{str(player1.hp)} hp", True, WHITE), relres(480, 900))
        
        # Vidas de jugador 1
        if player1.lives == 2:
            buffer_surface.blit(heart_image, relres(550, 997))
            buffer_surface.blit(heart_image, relres(515, 997))
            buffer_surface.blit(heart_image, relres(480, 997))
        elif player1.lives == 1:
            buffer_surface.blit(heart_image, relres(515, 997))
            buffer_surface.blit(heart_image, relres(480, 997))
        elif player1.lives == 0:
            buffer_surface.blit(heart_image, relres(480, 997))
            
    elif player1.lives < 0:
        buffer_surface.blit(title_font.render(translate("dead"), True, DARK_RED), relres(480, 900))

    # Icono de jugador 2
    buffer_surface.blit(player2.icon, relres(1315, 840))
    
    # Nombre de jugador 2
    player2_name_surface = font.render(player2.name, True, player2.color)
    player2_text_width = player2_name_surface.get_width()
    player2_text_width += relres(20)  # Añadir padding (espacio a los lados)
    pygame.draw.rect(buffer_surface, WHITE, relres(1315, 950, player2_text_width / SCREEN_WIDTH * 1920, 45), 0, 8)
    buffer_surface.blit(player2_name_surface, relres(1325, 955))
    
    # Vida de jugador 2
    if player2.lives >= 0:
        buffer_surface.blit(title_font.render(f"{str(player2.hp)} hp", True, WHITE), relres(1315, 900))
        
        # Vidas de jugador 2
        if player2.lives == 2:
            buffer_surface.blit(heart_image, relres(1385, 997))
            buffer_surface.blit(heart_image, relres(1350, 997))
            buffer_surface.blit(heart_image, relres(1315, 997))
        elif player2.lives == 1:
            buffer_surface.blit(heart_image, relres(1350, 997))
            buffer_surface.blit(heart_image, relres(1315, 997))
        elif player2.lives == 0:
            buffer_surface.blit(heart_image, relres(1315, 997))
    elif player2.lives < 0:
        buffer_surface.blit(title_font.render(translate("dead"), True, DARK_RED), relres(1315, 900))

    #Plataformas
    for platform in platforms:
        platform.draw(buffer_surface)
    
    #Jugadores
    for player in players:
        player.draw(buffer_surface)
    
    #Proyectiles
    for player in players:
        player.draw_projectiles(buffer_surface)
    
    # Etiquetas de nombre para los jugadores
    for player in players:
        player_nametag = small_font.render(player.name, True, hex_to_rgb(player.color))
        player_name_width = player_nametag.get_width() + 20
        player_name_height = relres(30)
        
        player_name_x = player.rect.x + (player.rect.width // 2) - (player_name_width // 2)
        player_name_y = player.rect.y - player_name_height - 10
        
        pygame.draw.rect(buffer_surface, WHITE, (player_name_x, player_name_y, player_name_width, player_name_height), 0, 8)
        buffer_surface.blit(player_nametag, (player_name_x + 10, player_name_y + 2))

    # Hitboxes y otra información debug (si están activadas)
    if debug:
        for platform in platforms:
            platform.draw_hitboxes(buffer_surface)

        for player in players:
            player.draw_hitboxes(buffer_surface)

        for projectile in player1.projectiles:
            projectile.draw_hitboxes(buffer_surface)

        for projectile in player2.projectiles:
            projectile.draw_hitboxes(buffer_surface)
        
        buffer_surface.blit(font.render(f"Player 1 status: {player1.status}", True, BLACK), relres(0, 0))
        buffer_surface.blit(font.render(f"Player 2 status: {player2.status}", True, BLACK), relres(0, 30))
        buffer_surface.blit(font.render(f"Player 1 inv.: {player1.invulnerable} ({int(player1.invulnerability_timer * 1000)} ms)", True, BLACK), relres(0, 60))
        buffer_surface.blit(font.render(f"Player 2 inv.: {player2.invulnerable} ({int(player2.invulnerability_timer * 1000)} ms)", True, BLACK), relres(0, 90))

    # Escalar la superficie "buffer" para ajustarse al tamaño de la ventana
    scaled_surface = pygame.transform.smoothscale(buffer_surface, (screen.get_width(), screen.get_height()))
    
    # Dibujar la superficie escalada en la pantalla
    screen.blit(scaled_surface, (0, 0))