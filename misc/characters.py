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

import pygame

pygame.init()
pygame.font.init()


################################################################################################
########################################## >> BERT << ##########################################
################################################################################################

BERT = {
    "name": "Bert",
    "description": "humano promedio.",
    "health": 100,
    "damage": 5,
    "projectile_damage": 3,
    "velocity": 5,
    "jump_velocity": 11,
    "crit_chance": 0.2,
    "gravity": 0.5,
    "terminal_velocity": 20,
    "weight": 1,
    "walking_sprites_right": [
        (pygame.image.load("assets/images/characters/bert/walk/0.png")),
        (pygame.image.load("assets/images/characters/bert/walk/1.png")),
        (pygame.image.load("assets/images/characters/bert/walk/2.png")),
        (pygame.image.load("assets/images/characters/bert/walk/3.png")),
        (pygame.image.load("assets/images/characters/bert/walk/4.png"))
    ],
    "walking_sprites_left": [],
    "jumping_sprites_right": [
        (pygame.image.load("assets/images/characters/bert/jump/0.png")),
        (pygame.image.load("assets/images/characters/bert/jump/1.png")),
        (pygame.image.load("assets/images/characters/bert/jump/2.png")),
        (pygame.image.load("assets/images/characters/bert/jump/3.png")),
        (pygame.image.load("assets/images/characters/bert/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    "idle_sprite_right": [(pygame.image.load("assets/images/characters/bert/idle/0.png"))],
    "idle_sprite_left": [],
    "attack_sprite_right": [(pygame.image.load("assets/images/characters/bert/attack/0.png"))],
    "attack_sprite_left": [],
    "damage_sprite_right": [(pygame.image.load("assets/images/characters/bert/damage/0.png"))],
    "damage_sprite_left": [],
    "icon": pygame.image.load("assets/images/characters/bert/icon.png")
}

for sprite in BERT["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERT["walking_sprites_left"].append(inverted_sprite)

for sprite in BERT["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERT["jumping_sprites_left"].append(inverted_sprite)

BERT["idle_sprite_left"] = [(pygame.transform.flip(BERT["idle_sprite_right"][0], True, False))]

BERT["attack_sprite_left"] = [(pygame.transform.flip(BERT["attack_sprite_right"][0], True, False))]

BERT["damage_sprite_left"] = [(pygame.transform.flip(BERT["damage_sprite_right"][0], True, False))]


################################################################################################
######################################### >> BERROTA << ########################################
################################################################################################

BERROTA = {
    "name": "Berrota",
    "description": "chaval flaco que se mueve rápido",
    "health": 90,
    "damage": 5,
    "projectile_damage": 3,
    "velocity": 7,
    "jump_velocity": 13,
    "crit_chance": 0.35,
    "gravity": 0.5,
    "terminal_velocity": 17,
    "weight": 1.5,
    "walking_sprites_right": [
        (pygame.image.load("assets/images/characters/berrota/walk/0.png")),
        (pygame.image.load("assets/images/characters/berrota/walk/1.png")),
        (pygame.image.load("assets/images/characters/berrota/walk/2.png")),
        (pygame.image.load("assets/images/characters/berrota/walk/3.png")),
        (pygame.image.load("assets/images/characters/berrota/walk/4.png"))
    ],
    "walking_sprites_left": [],
    "jumping_sprites_right": [
        (pygame.image.load("assets/images/characters/berrota/jump/0.png")),
        (pygame.image.load("assets/images/characters/berrota/jump/1.png")),
        (pygame.image.load("assets/images/characters/berrota/jump/2.png")),
        (pygame.image.load("assets/images/characters/berrota/jump/3.png")),
        (pygame.image.load("assets/images/characters/berrota/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    "idle_sprite_right": [(pygame.image.load("assets/images/characters/berrota/idle/0.png"))],
    "idle_sprite_left": [],
    "attack_sprite_right": [(pygame.image.load("assets/images/characters/berrota/attack/0.png"))],
    "attack_sprite_left": [],
    "damage_sprite_right": [(pygame.image.load("assets/images/characters/berrota/damage/0.png"))],
    "damage_sprite_left": [],
    "icon": pygame.image.load("assets/images/characters/berrota/icon.png")
}

for sprite in BERROTA["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERROTA["walking_sprites_left"].append(inverted_sprite)

for sprite in BERROTA["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERROTA["jumping_sprites_left"].append(inverted_sprite)

BERROTA["idle_sprite_left"] = [(pygame.transform.flip(BERROTA["idle_sprite_right"][0], True, False))]

BERROTA["attack_sprite_left"] = [(pygame.transform.flip(BERROTA["attack_sprite_right"][0], True, False))]

BERROTA["damage_sprite_left"] = [(pygame.transform.flip(BERROTA["damage_sprite_right"][0], True, False))]


################################################################################################
########################################## >> LORC << ##########################################
################################################################################################

LORC = {
    "name": "Lorc",
    "description": "Tipo tanque, su único punto débil es la gravedad.",
    "health": 200,
    "damage": 5,
    "projectile_damage": 3,
    "velocity": 3,
    "jump_velocity": 7.5,
    "crit_chance": 0.1,
    "gravity": 0.72,
    "terminal_velocity": 25,
    "weight": 0.5,
    "walking_sprites_right": [
        (pygame.image.load("assets/images/characters/lorc/walk/0.png")),
        (pygame.image.load("assets/images/characters/lorc/walk/1.png")),
        (pygame.image.load("assets/images/characters/lorc/walk/2.png")),
        (pygame.image.load("assets/images/characters/lorc/walk/3.png")),
        (pygame.image.load("assets/images/characters/lorc/walk/4.png"))
    ],
    "walking_sprites_left": [],
    "jumping_sprites_right": [
        (pygame.image.load("assets/images/characters/lorc/jump/0.png")),
        (pygame.image.load("assets/images/characters/lorc/jump/1.png")),
        (pygame.image.load("assets/images/characters/lorc/jump/2.png")),
        (pygame.image.load("assets/images/characters/lorc/jump/3.png")),
        (pygame.image.load("assets/images/characters/lorc/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    "idle_sprite_right": [(pygame.image.load("assets/images/characters/lorc/idle/0.png"))],
    "idle_sprite_left": [],
    "attack_sprite_right": [(pygame.image.load("assets/images/characters/lorc/attack/0.png"))],
    "attack_sprite_left": [],
    "damage_sprite_right": [(pygame.image.load("assets/images/characters/lorc/damage/0.png"))],
    "damage_sprite_left": [],
    "icon": pygame.image.load("assets/images/characters/lorc/icon.png")
}

for sprite in LORC["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    LORC["walking_sprites_left"].append(inverted_sprite)

for sprite in LORC["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    LORC["jumping_sprites_left"].append(inverted_sprite)

LORC["idle_sprite_left"] = [(pygame.transform.flip(LORC["idle_sprite_right"][0], True, False))]

LORC["attack_sprite_left"] = [(pygame.transform.flip(LORC["attack_sprite_right"][0], True, False))]

LORC["damage_sprite_left"] = [(pygame.transform.flip(LORC["damage_sprite_right"][0], True, False))]


################################################################################################
########################################## >> JORDI << #########################################
################################################################################################

JORDI = {
    "name": "Jordi",
    "description": "Es gay. Poca vida pero daño alto. Es gay.",
    "health": 80,
    "damage": 10,
    "projectile_damage": 5,
    "velocity": 5.1,
    "jump_velocity": 11,
    "crit_chance": 0.3,
    "gravity": 0.5,
    "terminal_velocity": 17,
    "weight": 1.2,
    "walking_sprites_right": [
        (pygame.image.load("assets/images/characters/jordi/walk/0.png")),
        (pygame.image.load("assets/images/characters/jordi/walk/1.png")),
        (pygame.image.load("assets/images/characters/jordi/walk/2.png")),
        (pygame.image.load("assets/images/characters/jordi/walk/3.png")),
        (pygame.image.load("assets/images/characters/jordi/walk/4.png"))
    ],
    "walking_sprites_left": [],
    "jumping_sprites_right": [
        (pygame.image.load("assets/images/characters/jordi/jump/0.png")),
        (pygame.image.load("assets/images/characters/jordi/jump/1.png")),
        (pygame.image.load("assets/images/characters/jordi/jump/2.png")),
        (pygame.image.load("assets/images/characters/jordi/jump/3.png")),
        (pygame.image.load("assets/images/characters/jordi/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    "idle_sprite_right": [(pygame.image.load("assets/images/characters/jordi/idle/0.png"))],
    "idle_sprite_left": [],
    "attack_sprite_right": [(pygame.image.load("assets/images/characters/jordi/attack/0.png"))],
    "attack_sprite_left": [],
    "damage_sprite_right": [(pygame.image.load("assets/images/characters/jordi/damage/0.png"))],
    "damage_sprite_left": [],
    "icon": pygame.image.load("assets/images/characters/jordi/icon.png")
}

for sprite in JORDI["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    JORDI["walking_sprites_left"].append(inverted_sprite)

for sprite in JORDI["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    JORDI["jumping_sprites_left"].append(inverted_sprite)

JORDI["idle_sprite_left"] = [(pygame.transform.flip(JORDI["idle_sprite_right"][0], True, False))]

JORDI["attack_sprite_left"] = [(pygame.transform.flip(JORDI["attack_sprite_right"][0], True, False))]

JORDI["damage_sprite_left"] = [(pygame.transform.flip(JORDI["damage_sprite_right"][0], True, False))]

################################################################################################
########################################## >> BARCOS << ########################################
################################################################################################

BARCOS = {
    "name": "Barcos",
    "description": "Habilidad especial: morderte los tobillos.",
    "health": 80,
    "damage": 9,
    "projectile_damage": 6,
    "velocity": 10,
    "jump_velocity": 12,
    "crit_chance": 0.6,
    "gravity": 0.5,
    "terminal_velocity": 17,
    "weight": 1,
    "walking_sprites_right": [
        (pygame.image.load("assets/images/characters/barcos/walk/0.png")),
        (pygame.image.load("assets/images/characters/barcos/walk/1.png")),
        (pygame.image.load("assets/images/characters/barcos/walk/2.png")),
        (pygame.image.load("assets/images/characters/barcos/walk/3.png")),
        (pygame.image.load("assets/images/characters/barcos/walk/4.png"))
    ],
    "walking_sprites_left": [],
    "jumping_sprites_right": [
        (pygame.image.load("assets/images/characters/barcos/jump/0.png")),
        (pygame.image.load("assets/images/characters/barcos/jump/1.png")),
        (pygame.image.load("assets/images/characters/barcos/jump/2.png")),
        (pygame.image.load("assets/images/characters/barcos/jump/3.png")),
        (pygame.image.load("assets/images/characters/barcos/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    "idle_sprite_right": [(pygame.image.load("assets/images/characters/barcos/idle/0.png"))],
    "idle_sprite_left": [],
    "attack_sprite_right": [(pygame.image.load("assets/images/characters/barcos/attack/0.png"))],
    "attack_sprite_left": [],
    "damage_sprite_right": [(pygame.image.load("assets/images/characters/barcos/damage/0.png"))],
    "damage_sprite_left": [],
    "icon": pygame.image.load("assets/images/characters/barcos/icon.png")
}

for sprite in BARCOS["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BARCOS["walking_sprites_left"].append(inverted_sprite)

for sprite in BARCOS["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BARCOS["jumping_sprites_left"].append(inverted_sprite)

BARCOS["idle_sprite_left"] = [(pygame.transform.flip(BARCOS["idle_sprite_right"][0], True, False))]

BARCOS["attack_sprite_left"] = [(pygame.transform.flip(BARCOS["attack_sprite_right"][0], True, False))]

BARCOS["damage_sprite_left"] = [(pygame.transform.flip(BARCOS["damage_sprite_right"][0], True, False))]

################################################################################################
######################################### >> ALSEXITO << #######################################
################################################################################################

ALSEXITO = {
    "name": "Alsexito",
    "description": "En cuanto menos de lo esperas ya te está dando por detrás",
    "health": 170,
    "damage": 30,
    "projectile_damage": 1,
    "velocity": 2.8,
    "jump_velocity": 8,
    "crit_chance": 0.69420,
    "gravity": 0.7,
    "terminal_velocity": 30,
    "weight": 2,
    "walking_sprites_right": [
        (pygame.image.load("assets/images/characters/alsexito/walk/0.png")),
        (pygame.image.load("assets/images/characters/alsexito/walk/1.png")),
        (pygame.image.load("assets/images/characters/alsexito/walk/2.png")),
        (pygame.image.load("assets/images/characters/alsexito/walk/3.png")),
        (pygame.image.load("assets/images/characters/alsexito/walk/4.png"))
    ],
    "walking_sprites_left": [],
    "jumping_sprites_right": [
        (pygame.image.load("assets/images/characters/alsexito/jump/0.png")),
        (pygame.image.load("assets/images/characters/alsexito/jump/1.png")),
        (pygame.image.load("assets/images/characters/alsexito/jump/2.png")),
        (pygame.image.load("assets/images/characters/alsexito/jump/3.png")),
        (pygame.image.load("assets/images/characters/alsexito/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    "idle_sprite_right": [(pygame.image.load("assets/images/characters/alsexito/idle/0.png"))],
    "idle_sprite_left": [],
    "attack_sprite_right": [(pygame.image.load("assets/images/characters/alsexito/attack/0.png"))],
    "attack_sprite_left": [],
    "damage_sprite_right": [(pygame.image.load("assets/images/characters/alsexito/damage/0.png"))],
    "damage_sprite_left": [],
    "icon": pygame.image.load("assets/images/characters/alsexito/icon.png")
}

for sprite in ALSEXITO["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    ALSEXITO["walking_sprites_left"].append(inverted_sprite)

for sprite in ALSEXITO["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    ALSEXITO["jumping_sprites_left"].append(inverted_sprite)

ALSEXITO["idle_sprite_left"] = [(pygame.transform.flip(ALSEXITO["idle_sprite_right"][0], True, False))]

ALSEXITO["attack_sprite_left"] = [(pygame.transform.flip(ALSEXITO["attack_sprite_right"][0], True, False))]

ALSEXITO["damage_sprite_left"] = [(pygame.transform.flip(ALSEXITO["damage_sprite_right"][0], True, False))]