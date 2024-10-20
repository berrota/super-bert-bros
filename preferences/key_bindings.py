import pygame

#Para cambiar los controles, encuentra la tecla respectiva en esta lista: http://cs.roanoke.edu/Fall2013/CPSC120A/pygame-1.9.1-docs-html/ref/key.html
#... y después de añadir un "pygame." al principio, sustituye la acción que quieras modificar aquí abajo
#Si quieres que una acción no se active con ninguna tecla, usa pygame.K_UNKNOWN


####################################### JUGADOR 1 #######################################

K_player1_left = pygame.K_a #izquierda
K_player1_right = pygame.K_d #derecha
K_player1_jump = pygame.K_SPACE #saltar

K_player1_projectile = pygame.K_e #proyectil
K_player1_attack = pygame.K_w

####################################### JUGADOR 2 #######################################

K_player2_left = pygame.K_LEFT #izquierda
K_player2_right = pygame.K_RIGHT #derecha
K_player2_jump = pygame.K_UP #saltar

K_player2_projectile = pygame.K_RCTRL #proyectil
K_player2_attack = pygame.K_END

####################################### OTROS #######################################

K_debug = pygame.K_b #mostrar información de debug
K_pause = pygame.K_ESCAPE #menú de pausa
K_quit = pygame.K_0 #cerrar el juego
K_fullscreen = pygame.K_F11 #pantalla completa