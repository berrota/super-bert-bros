#Si quieres cambiar las stats de algún personaje, utiliza esto como un índice:
"""
name: nombre
description: descripción
health: puntos de vida
damage: daño melee (de momento inútil)
projectile_damage: daño de proyectil
velocity: velocidad
jump_velocity: intensidad de salto
crit_chance: probabilidad de golpe crítico (de momento inútil)
gravity: intensidad de la gravedad
terminal_velocity: máxima velocidad alcanzable
weight: peso (sirve para calcular el empuje de un golpe). cuanto menor sea mayor empuje recibirá
walking_sprites_right: sprites de caminar hacia la derecha
walking_sprites_left: sprites de caminar hacia la izquierda
... lo mismo con jump_sprites, idle_sprite, attack_sprite y damage_sprite
icon: icono que se muestra en la parte inferior de la pantalla
"""

from misc.files import load_sprite
from util.translator import translate

import pygame

pygame.init()
pygame.font.init()


################################################################################################
########################################## >> BERT << ##########################################
################################################################################################

BERT = {
    #Nombre y descripción
    "name": "Bert",
    "description": translate("bert.description"),
    
    #Vida y daño
    "health": 100,
    "damage": 5,
    "projectile_damage": 3,
    "crit_chance": 0.2,
    
    #Movimiento
    "velocity": 5,
    "jump_velocity": 11,
    "terminal_velocity": 20,
    "gravity": 0.5,
    "weight": 1,
    
    #Sprites y animaciones
    "walking_sprites_right": [
        (load_sprite("assets/images/characters/bert/walk/0.png")),
        (load_sprite("assets/images/characters/bert/walk/1.png")),
        (load_sprite("assets/images/characters/bert/walk/2.png")),
        (load_sprite("assets/images/characters/bert/walk/3.png")),
        (load_sprite("assets/images/characters/bert/walk/4.png"))
    ],
    "walking_sprites_left": [],
    
    "jumping_sprites_right": [
        (load_sprite("assets/images/characters/bert/jump/0.png")),
        (load_sprite("assets/images/characters/bert/jump/1.png")),
        (load_sprite("assets/images/characters/bert/jump/2.png")),
        (load_sprite("assets/images/characters/bert/jump/3.png")),
        (load_sprite("assets/images/characters/bert/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    
    "idle_sprite_right": [(load_sprite("assets/images/characters/bert/idle/0.png"))],
    "idle_sprite_left": [],
    
    "shoot_sprite_right": [(load_sprite("assets/images/characters/bert/shoot/0.png"))],
    "shoot_sprite_left": [],
    
    "attack_sprites_right": [
        (load_sprite("assets/images/characters/bert/attack/0.png")),
        (load_sprite("assets/images/characters/bert/attack/1.png")),
        (load_sprite("assets/images/characters/bert/attack/2.png")),
        (load_sprite("assets/images/characters/bert/attack/3.png")),
        (load_sprite("assets/images/characters/bert/attack/4.png"))
    ],
    "attack_sprites_left": [],
    
    "damage_sprite_right": [(load_sprite("assets/images/characters/bert/damage/0.png"))],
    "damage_sprite_left": [],
    
    "icon": load_sprite("assets/images/characters/bert/icon.png"),
    "icon_dead": load_sprite("assets/images/characters/bert/icon_dead.png")
}

#Invertir sprites de derecha para obtener sprites de izquierda
for sprite in BERT["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERT["walking_sprites_left"].append(inverted_sprite)

for sprite in BERT["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERT["jumping_sprites_left"].append(inverted_sprite)

for sprite in BERT["attack_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERT["attack_sprites_left"].append(inverted_sprite)

BERT["idle_sprite_left"] = [(pygame.transform.flip(BERT["idle_sprite_right"][0], True, False))]

BERT["shoot_sprite_left"] = [(pygame.transform.flip(BERT["shoot_sprite_right"][0], True, False))]

BERT["damage_sprite_left"] = [(pygame.transform.flip(BERT["damage_sprite_right"][0], True, False))]


################################################################################################
######################################### >> BERROTA << ########################################
################################################################################################

BERROTA = {
    "name": "Berrota",
    "description": translate("berrota.description"),
    
    "health": 90,
    "damage": 5,
    "projectile_damage": 3,
    "crit_chance": 0.35,
    
    "velocity": 7,
    "jump_velocity": 13,
    "terminal_velocity": 17,
    "gravity": 0.5,
    "weight": 0.5,
    
    "walking_sprites_right": [
        (load_sprite("assets/images/characters/berrota/walk/0.png")),
        (load_sprite("assets/images/characters/berrota/walk/1.png")),
        (load_sprite("assets/images/characters/berrota/walk/2.png")),
        (load_sprite("assets/images/characters/berrota/walk/3.png")),
        (load_sprite("assets/images/characters/berrota/walk/4.png"))
    ],
    "walking_sprites_left": [],
    
    "jumping_sprites_right": [
        (load_sprite("assets/images/characters/berrota/jump/0.png")),
        (load_sprite("assets/images/characters/berrota/jump/1.png")),
        (load_sprite("assets/images/characters/berrota/jump/2.png")),
        (load_sprite("assets/images/characters/berrota/jump/3.png")),
        (load_sprite("assets/images/characters/berrota/jump/4.png"))
    ],
    "jumping_sprites_left": [],
        
    "attack_sprites_right": [
        (load_sprite("assets/images/characters/berrota/attack/0.png")),
        (load_sprite("assets/images/characters/berrota/attack/1.png")),
        (load_sprite("assets/images/characters/berrota/attack/2.png")),
        (load_sprite("assets/images/characters/berrota/attack/3.png")),
        (load_sprite("assets/images/characters/berrota/attack/4.png"))
    ],
    "attack_sprites_left": [],
    
    "idle_sprite_right": [(load_sprite("assets/images/characters/berrota/idle/0.png"))],
    "idle_sprite_left": [],
    
    "shoot_sprite_right": [(load_sprite("assets/images/characters/berrota/shoot/0.png"))],
    "shoot_sprite_left": [],
    
    "damage_sprite_right": [(load_sprite("assets/images/characters/berrota/damage/0.png"))],
    "damage_sprite_left": [],
    
    "icon": load_sprite("assets/images/characters/berrota/icon.png"),
    "icon_dead": load_sprite("assets/images/characters/berrota/icon_dead.png")
}

for sprite in BERROTA["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERROTA["walking_sprites_left"].append(inverted_sprite)

for sprite in BERROTA["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERROTA["jumping_sprites_left"].append(inverted_sprite)

for sprite in BERROTA["attack_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERROTA["attack_sprites_left"].append(inverted_sprite)

BERROTA["idle_sprite_left"] = [(pygame.transform.flip(BERROTA["idle_sprite_right"][0], True, False))]

BERROTA["shoot_sprite_left"] = [(pygame.transform.flip(BERROTA["shoot_sprite_right"][0], True, False))]

BERROTA["damage_sprite_left"] = [(pygame.transform.flip(BERROTA["damage_sprite_right"][0], True, False))]


################################################################################################
########################################## >> LORC << ##########################################
################################################################################################

LORC = {
    "name": "Lorc",
    "description": translate("lorc.description"),
    
    "health": 200,
    "damage": 5,
    "projectile_damage": 3,
    "crit_chance": 0.1,
    
    "velocity": 3,
    "jump_velocity": 7.5,
    "terminal_velocity": 25,
    "gravity": 0.72,
    "weight": 2,
    
    "walking_sprites_right": [
        (load_sprite("assets/images/characters/lorc/walk/0.png")),
        (load_sprite("assets/images/characters/lorc/walk/1.png")),
        (load_sprite("assets/images/characters/lorc/walk/2.png")),
        (load_sprite("assets/images/characters/lorc/walk/3.png")),
        (load_sprite("assets/images/characters/lorc/walk/4.png"))
    ],
    "walking_sprites_left": [],
    
    "jumping_sprites_right": [
        (load_sprite("assets/images/characters/lorc/jump/0.png")),
        (load_sprite("assets/images/characters/lorc/jump/1.png")),
        (load_sprite("assets/images/characters/lorc/jump/2.png")),
        (load_sprite("assets/images/characters/lorc/jump/3.png")),
        (load_sprite("assets/images/characters/lorc/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    
    "attack_sprites_right": [
        (load_sprite("assets/images/characters/lorc/attack/0.png")),
        (load_sprite("assets/images/characters/lorc/attack/1.png")),
        (load_sprite("assets/images/characters/lorc/attack/2.png")),
        (load_sprite("assets/images/characters/lorc/attack/3.png")),
        (load_sprite("assets/images/characters/lorc/attack/4.png"))
    ],
    "attack_sprites_left": [],
    
    "idle_sprite_right": [(load_sprite("assets/images/characters/lorc/idle/0.png"))],
    "idle_sprite_left": [],
    
    "shoot_sprite_right": [(load_sprite("assets/images/characters/lorc/shoot/0.png"))],
    "shoot_sprite_left": [],
    
    "damage_sprite_right": [(load_sprite("assets/images/characters/lorc/damage/0.png"))],
    "damage_sprite_left": [],
    
    "icon": load_sprite("assets/images/characters/lorc/icon.png"),
    "icon_dead": load_sprite("assets/images/characters/lorc/icon_dead.png")
}

for sprite in LORC["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    LORC["walking_sprites_left"].append(inverted_sprite)

for sprite in LORC["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    LORC["jumping_sprites_left"].append(inverted_sprite)

for sprite in LORC["attack_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    LORC["attack_sprites_left"].append(inverted_sprite)

LORC["idle_sprite_left"] = [(pygame.transform.flip(LORC["idle_sprite_right"][0], True, False))]

LORC["shoot_sprite_left"] = [(pygame.transform.flip(LORC["shoot_sprite_right"][0], True, False))]

LORC["damage_sprite_left"] = [(pygame.transform.flip(LORC["damage_sprite_right"][0], True, False))]


################################################################################################
########################################## >> JORDI << #########################################
################################################################################################

JORDI = {
    "name": "Jordi",
    "description": translate("jordi.description"),
    
    "health": 80,
    "damage": 10,
    "projectile_damage": 5,
    "crit_chance": 0.3,
    
    "velocity": 5.1,
    "jump_velocity": 11,
    "terminal_velocity": 17,
    "gravity": 0.5,
    "weight": 1.2,
    
    "walking_sprites_right": [
        (load_sprite("assets/images/characters/jordi/walk/0.png")),
        (load_sprite("assets/images/characters/jordi/walk/1.png")),
        (load_sprite("assets/images/characters/jordi/walk/2.png")),
        (load_sprite("assets/images/characters/jordi/walk/3.png")),
        (load_sprite("assets/images/characters/jordi/walk/4.png"))
    ],
    "walking_sprites_left": [],
    
    "jumping_sprites_right": [
        (load_sprite("assets/images/characters/jordi/jump/0.png")),
        (load_sprite("assets/images/characters/jordi/jump/1.png")),
        (load_sprite("assets/images/characters/jordi/jump/2.png")),
        (load_sprite("assets/images/characters/jordi/jump/3.png")),
        (load_sprite("assets/images/characters/jordi/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    
    "attack_sprites_right": [
        (load_sprite("assets/images/characters/jordi/attack/0.png")),
        (load_sprite("assets/images/characters/jordi/attack/1.png")),
        (load_sprite("assets/images/characters/jordi/attack/2.png")),
        (load_sprite("assets/images/characters/jordi/attack/3.png")),
        (load_sprite("assets/images/characters/jordi/attack/4.png"))
    ],
    "attack_sprites_left": [],
    
    "idle_sprite_right": [(load_sprite("assets/images/characters/jordi/idle/0.png"))],
    "idle_sprite_left": [],
    
    "shoot_sprite_right": [(load_sprite("assets/images/characters/jordi/shoot/0.png"))],
    "shoot_sprite_left": [],
    
    "damage_sprite_right": [(load_sprite("assets/images/characters/jordi/damage/0.png"))],
    "damage_sprite_left": [],
    
    "icon": load_sprite("assets/images/characters/jordi/icon.png"),
    "icon_dead": load_sprite("assets/images/characters/jordi/icon_dead.png")
}

for sprite in JORDI["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    JORDI["walking_sprites_left"].append(inverted_sprite)

for sprite in JORDI["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    JORDI["jumping_sprites_left"].append(inverted_sprite)
    
for sprite in JORDI["attack_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    JORDI["attack_sprites_left"].append(inverted_sprite)

JORDI["idle_sprite_left"] = [(pygame.transform.flip(JORDI["idle_sprite_right"][0], True, False))]

JORDI["shoot_sprite_left"] = [(pygame.transform.flip(JORDI["shoot_sprite_right"][0], True, False))]

JORDI["damage_sprite_left"] = [(pygame.transform.flip(JORDI["damage_sprite_right"][0], True, False))]

################################################################################################
########################################## >> BARCOS << ########################################
################################################################################################

BARCOS = {
    "name": "Barcos",
    "description": translate("barcos.description"),
    
    "health": 80,
    "damage": 9,
    "projectile_damage": 6,
    "crit_chance": 0.6,
    
    "velocity": 10,
    "jump_velocity": 12,
    "terminal_velocity": 17,
    "gravity": 0.5,
    "weight": 0.25,
    
    "walking_sprites_right": [
        (load_sprite("assets/images/characters/barcos/walk/0.png")),
        (load_sprite("assets/images/characters/barcos/walk/1.png")),
        (load_sprite("assets/images/characters/barcos/walk/2.png")),
        (load_sprite("assets/images/characters/barcos/walk/3.png")),
        (load_sprite("assets/images/characters/barcos/walk/4.png"))
    ],
    "walking_sprites_left": [],
    
    "jumping_sprites_right": [
        (load_sprite("assets/images/characters/barcos/jump/0.png")),
        (load_sprite("assets/images/characters/barcos/jump/1.png")),
        (load_sprite("assets/images/characters/barcos/jump/2.png")),
        (load_sprite("assets/images/characters/barcos/jump/3.png")),
        (load_sprite("assets/images/characters/barcos/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    
    "attack_sprites_right": [
        (load_sprite("assets/images/characters/barcos/attack/0.png")),
        (load_sprite("assets/images/characters/barcos/attack/1.png")),
        (load_sprite("assets/images/characters/barcos/attack/2.png")),
        (load_sprite("assets/images/characters/barcos/attack/3.png")),
        (load_sprite("assets/images/characters/barcos/attack/4.png"))
    ],
    "attack_sprites_left": [],
    
    "idle_sprite_right": [(load_sprite("assets/images/characters/barcos/idle/0.png"))],
    "idle_sprite_left": [],
    
    "shoot_sprite_right": [(load_sprite("assets/images/characters/barcos/shoot/0.png"))],
    "shoot_sprite_left": [],
    
    "damage_sprite_right": [(load_sprite("assets/images/characters/barcos/damage/0.png"))],
    "damage_sprite_left": [],
    
    "icon": load_sprite("assets/images/characters/barcos/icon.png"),
    "icon_dead": load_sprite("assets/images/characters/barcos/icon_dead.png")
}

for sprite in BARCOS["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BARCOS["walking_sprites_left"].append(inverted_sprite)

for sprite in BARCOS["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BARCOS["jumping_sprites_left"].append(inverted_sprite)
    
for sprite in BARCOS["attack_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BARCOS["attack_sprites_left"].append(inverted_sprite)

BARCOS["idle_sprite_left"] = [(pygame.transform.flip(BARCOS["idle_sprite_right"][0], True, False))]

BARCOS["shoot_sprite_left"] = [(pygame.transform.flip(BARCOS["shoot_sprite_right"][0], True, False))]

BARCOS["damage_sprite_left"] = [(pygame.transform.flip(BARCOS["damage_sprite_right"][0], True, False))]

################################################################################################
######################################### >> ALSEXITO << #######################################
################################################################################################

ALSEXITO = {
    "name": "Alsexito",
    "description": translate("alsexito.description"),
    
    "health": 170,
    "damage": 30,
    "projectile_damage": 1,
    "crit_chance": 0.69420,
    
    "velocity": 2.8,
    "jump_velocity": 8,
    "terminal_velocity": 30,
    "gravity": 0.7,
    "weight": 1.7,
    
    "walking_sprites_right": [
        (load_sprite("assets/images/characters/alsexito/walk/0.png")),
        (load_sprite("assets/images/characters/alsexito/walk/1.png")),
        (load_sprite("assets/images/characters/alsexito/walk/2.png")),
        (load_sprite("assets/images/characters/alsexito/walk/3.png")),
        (load_sprite("assets/images/characters/alsexito/walk/4.png"))
    ],
    "walking_sprites_left": [],
    
    "jumping_sprites_right": [
        (load_sprite("assets/images/characters/alsexito/jump/0.png")),
        (load_sprite("assets/images/characters/alsexito/jump/1.png")),
        (load_sprite("assets/images/characters/alsexito/jump/2.png")),
        (load_sprite("assets/images/characters/alsexito/jump/3.png")),
        (load_sprite("assets/images/characters/alsexito/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    
    "attack_sprites_right": [
        (load_sprite("assets/images/characters/alsexito/attack/0.png")),
        (load_sprite("assets/images/characters/alsexito/attack/1.png")),
        (load_sprite("assets/images/characters/alsexito/attack/2.png")),
        (load_sprite("assets/images/characters/alsexito/attack/3.png")),
        (load_sprite("assets/images/characters/alsexito/attack/4.png"))
    ],
    "attack_sprites_left": [],
    
    "idle_sprite_right": [(load_sprite("assets/images/characters/alsexito/idle/0.png"))],
    "idle_sprite_left": [],
    
    "shoot_sprite_right": [(load_sprite("assets/images/characters/alsexito/shoot/0.png"))],
    "shoot_sprite_left": [],
    
    "damage_sprite_right": [(load_sprite("assets/images/characters/alsexito/damage/0.png"))],
    "damage_sprite_left": [],
    
    "icon": load_sprite("assets/images/characters/alsexito/icon.png"),
    "icon_dead": load_sprite("assets/images/characters/alsexito/icon_dead.png")
}

for sprite in ALSEXITO["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    ALSEXITO["walking_sprites_left"].append(inverted_sprite)

for sprite in ALSEXITO["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    ALSEXITO["jumping_sprites_left"].append(inverted_sprite)
    
for sprite in ALSEXITO["attack_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    ALSEXITO["attack_sprites_left"].append(inverted_sprite)

ALSEXITO["idle_sprite_left"] = [(pygame.transform.flip(ALSEXITO["idle_sprite_right"][0], True, False))]

ALSEXITO["shoot_sprite_left"] = [(pygame.transform.flip(ALSEXITO["shoot_sprite_right"][0], True, False))]

ALSEXITO["damage_sprite_left"] = [(pygame.transform.flip(ALSEXITO["damage_sprite_right"][0], True, False))]