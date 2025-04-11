import pygame
import screeninfo

pygame.init()

#Constantes que puse aquí por que no sé dónde si no ponerlas
SCREEN_WIDTH: int = 1366 #screeninfo.get_monitors()[0].width
SCREEN_HEIGHT: int = 768 #screeninfo.get_monitors()[0].height

FPS: int = 60

####################################### FUNCIONES DE AYUDA #######################################

def relres(x: int = None, y: int = None, w: int = None, h: int = None) -> tuple:
    """Ajusta las dimensiones para mantener proporción con el tamaño de la pantalla."""
    newres = (
        x / 1920 * SCREEN_WIDTH if x is not None else None,
        y / 1080 * SCREEN_HEIGHT if y is not None else None,
        w / 1920 * SCREEN_WIDTH if w is not None else None,
        h / 1080 * SCREEN_HEIGHT if h is not None else None
    )
    ret = tuple(n for n in newres if n is not None)
    return ret if len(ret) > 1 else ret[0]

def load_sprite(source: str) -> pygame.Surface:
    """Wrapper para cargar sprites que ajusta su tamaño concorde al de la pantalla."""
    image = pygame.image.load(source)
    return pygame.transform.scale(
        image, relres(image.get_width(), image.get_height())
    )

####################################### SPRITES #######################################

big_platform_image = load_sprite("assets/images/platform/platform_big.png")
small_platform_image = load_sprite("assets/images/platform/platform_small.png")

projectile_image_right = load_sprite("assets/images/projectile/projectile.png")
projectile_image_left = pygame.transform.flip(projectile_image_right, True, False)

heart_image = load_sprite("assets/images/ui/heart.png")

bg_image = pygame.image.load("assets/images/ui/background.png")
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


####################################### FUENTES DE LETRA #######################################

title_font = pygame.font.Font(None, int(relres(80)))
font = pygame.font.Font(None, int(relres(50)))
small_font = pygame.font.Font(None, int(relres(35)))


####################################### EFECTOS DE SONIDO Y MÚSICA #######################################

pygame.mixer.music.load("assets/sound/music.mp3")

jump_sound = pygame.mixer.Sound("assets/sound/jump.wav")
jump_sound2 = pygame.mixer.Sound("assets/sound/jump2.wav")
attack_sound = pygame.mixer.Sound("assets/sound/punch.mp3")
death_sound = pygame.mixer.Sound("assets/sound/death.wav")
projectile_sound = pygame.mixer.Sound("assets/sound/projectile.mp3")
void_death_sound = pygame.mixer.Sound("assets/sound/void_death.wav")
damage_sound = pygame.mixer.Sound("assets/sound/damage.wav")
game_end_sound = pygame.mixer.Sound("assets/sound/game_end.wav") 

#Ajuste de volumen para no romperte los tímpanos

pygame.mixer.music.set_volume(0.07)

jump_sound.set_volume(0.5)
jump_sound2.set_volume(0.2)
attack_sound.set_volume(0.7)
death_sound.set_volume(0.9)
projectile_sound.set_volume(0.2)
void_death_sound.set_volume(0.07)
damage_sound.set_volume(0.8)
game_end_sound.set_volume(0.1)