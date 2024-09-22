import pygame
import screeninfo

pygame.init()

####################################### SPRITES #######################################

platform_image = pygame.image.load("assets/images/platform/platform_big.png")
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

jump_sound = pygame.mixer.Sound("assets/sound/jump.wav")
jump_sound2 = pygame.mixer.Sound("assets/sound/jump2.wav")
death_sound = pygame.mixer.Sound("assets/sound/death.wav")
projectile_sound = pygame.mixer.Sound("assets/sound/projectile.wav")
void_death_sound = pygame.mixer.Sound("assets/sound/void_death.wav")
damage_sound = pygame.mixer.Sound("assets/sound/damage.wav")
game_end_sound = pygame.mixer.Sound("assets/sound/game_end.wav")

#Ajuste de volumen para los sonidos
jump_sound.set_volume(0.5)
jump_sound2.set_volume(0.2)
death_sound.set_volume(0.9)
projectile_sound.set_volume(0.2)
void_death_sound.set_volume(0.07)
damage_sound.set_volume(0.8)
game_end_sound.set_volume(0.1)