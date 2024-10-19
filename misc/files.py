import pygame
import screeninfo

pygame.init()

#Constantes que puse aquí por que no sé dónde si no ponerlas
SCREEN_WIDTH: int = 1920
SCREEN_HEIGHT: int = 1080

FPS: int = 60

####################################### SPRITES #######################################

big_platform_image = pygame.image.load("assets/images/platform/platform_big.png")
small_platform_image = pygame.image.load("assets/images/platform/platform_small.png")

projectile_image_right = pygame.image.load("assets/images/projectile/projectile.png")
projectile_image_left = pygame.transform.flip(projectile_image_right, True, False)

heart_image = pygame.image.load("assets/images/ui/heart.png")

for m in screeninfo.get_monitors():
    width = m.width
    height = m.height

bg_image = pygame.image.load("assets/images/ui/background.png")
bg_image = pygame.transform.scale(bg_image, (width, height))


####################################### FUENTES DE LETRA #######################################

title_font = pygame.font.Font(None, 80)
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 35)


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