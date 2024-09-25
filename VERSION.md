
# HISTORIAL DE CAMBIOS 

## v1.2 [25/IX/24]

### Agregado:
- Ahora se muestran las descripciones de los personajes al pasar el ratón por encima de la selección de personajes, dependiendo de qué personaje se ha elegido
- Cambiado de `VERSION.txt` a `VERSION.md`, para añadir formato y mayor legibilidad a este archivo
- Arreglado el bug donde se podía saltar aún no estando en plataformas
- Saltos dobles funcionales
- Mejorado las mecánicas de lanzamiento de proyectil y su animación, además de la de recibir daño
- Arreglado un bug donde el volumen de efectos sonoros no se manejaba correctamente
- Mejorado los reportes de crasheos
- Soporte para varios idiomas. Para cambiar tu idioma actual, vete a misc/options.py y cambia el valor `LANG` a uno que se encuentre en la carpeta [lang](/lang), sin la extensión `.json`. Por ejempo, `en_US` o `es_ES`.
- Los proyectiles ahora aparecen siempre a la misma distancia del centro del jugador sin importar hacia qué lado dispara
- Arreglado el bug donde los proyectiles podían traspasar la plataforma grande
- Mejoras al código (mayormente `game.py`) para seguir las directrices de PEP-8
- Ahora al cambiar de personajes en la mitad de la partida, ya no se te regenera la vida por completo, ahora tendrás la misma vida que antes, pero relativamente. Es decir si antes tenías 50 puntos de vida de 100 y te cambias el personaje a uno con 200 puntos de vida totales, tendrías 100
- Agregado idiomas para el archivo `README.md`


### Por añadir:
- Botón en el menú de pausa para poder ajustar las opciones de [options.py](options.py)
- Hacer uso de todas las opciones de [options.py](options.py)
- Ataques melee (ya me joderia tener que meter ataques melee en un juego de peleas). Me gustaría que la animación de ataque melee sea un gancho al estómago. Sin motivo alguno.
- Sé que parece una gilipollez, pero me gustaría añadir una animación donde Alsexito mueve las cejas al correr.
- Organizar un poco algunos archivos, donde todo está hecho una mierda y funciona porque Dios quiso
- Evitar conflicto de colores, que ambos jugadores no puedan llevar el mismo color
- Delta time (pero funcional)
- Eliminar sistema de puntos de vida y pasar a usar sistema de porcentaje como en el Smash
- Parries
- Más escenarios
- Funcionalidad mejorada a los sprites de ataque y daño
- Más SFX y música
- Ataques especiales
- Más mecánicas del Smash
- Arreglar cosas supongo


### Bugs ya conocidos:
- Al mover la ventana alrededor por unos segundos mientas no esté en pantalla completa, los personajes cambian de lugar. Creo que esto se debe a cómo se maneja el movimiento y el momentum de los personajes
- Resulta que por algún motivo ahora los personajes pueden aparecer debajo de las plataformes en vez de encima. Tiene que ver con estar mucho tiempo en la pantalla de selección de personajes
- Delta time hace que cuanto mayor sean los FPS menos se mueven los jugadores (relativamente) y viceversa
- Las hitboxes no se alinean perfectamente cuando un jugador se está moviendo o saltando.
- Por algún motivo que desconozco el juego puede crashear con código 3489660927. Se supone que está relacionado con errores de acceso de memoria o con el uso de pygame.mixer.Sound, probablemente el segundo

- Cuando tocas la parte lateral o inferior de una plataforma, te teletransporta encima de ella <-- esto lo voy a mantener como una mecánica más que un bug, lo más parecido que tengo a las mécanicas de "ledge" del Smash


## Frase de la semana:
> top sinco niños que sus padres están divorsiados pda pda pda pdapda pda pda pda 🗣️🗣️🗣️🔥🔥🔥💯‼️❗‼️ *-RANDOMLIFE*


con mucho amor, tu puta madre a cuatro
XOXO <3