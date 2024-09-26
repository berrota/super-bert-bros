
# HISTORIAL DE CAMBIOS 

## v1.3 [26/IX/24]

### Agregado:
- Ahora los dos jugadores no pueden llevar el mismo color ni nombre
- Al cerrar la ventana de selección de personajes se cierra el juego
- Eliminado el texto de debug de la esquina superior izquierda
- Corregido un error de ortografía en el README inglés
- Ahora los espacios no son carácteres válidos al seleccionar nombres de los jugadores, junto a más carácteres no alfanuméricos
- Botón en el menú de pausa para poder ajustar las opciones de [options.py](options.py)
- El texto de los botones en el menú de pausa ahora está centrado en ambos idiomas
- Creado carpeta `preferences` para guardar ahí las preferencias del usuario. Ahí se guardan los archivos `volume_prefs.py`, `options.py` y `key_bindings.py`
- Ahora los ajustes se guardan después de cerrar el juego y se cargan al abrirlo de nuevo, incluídos los de volumen
- Arreglado el bug donde los reportes de crasheos no se generaban porque el nombre del archivo contenía el caracter `:`
- Renombrado todo lo relacionado a disparar proyectiles (antes `attack`) a `shoot`, para reservarlo para lo relacionado a los ataques melee


### Por añadir:
- Ataques melee (ya me joderia tener que meter ataques melee en un juego de peleas). Me gustaría que la animación de ataque melee sea un gancho al estómago. Sin motivo alguno.
- Sé que parece una gilipollez, pero me gustaría añadir una animación donde Alsexito mueve las cejas al correr.
- Organizar un poco algunos archivos, donde todo está hecho una mierda y funciona porque Dios quiso
- Delta time (pero funcional)
- Eliminar sistema de puntos de vida y pasar a usar sistema de porcentaje como en el Smash
- Parries
- Más escenarios
- Más SFX y música
- Ataques especiales
- Más mecánicas del Smash
- Arreglar cosas supongo


### Bugs ya conocidos:
- Al mover la ventana alrededor por unos segundos mientas no esté en pantalla completa, los personajes cambian de lugar. Creo que esto se debe a cómo se maneja el movimiento y el momentum de los personajes
- Resulta que por algún motivo ahora los personajes pueden aparecer debajo de las plataformes en vez de encima. Tiene que ver con estar mucho tiempo en la pantalla de selección de personajes
- Delta time hace que cuanto mayor sean los FPS menos se mueven los jugadores (relativamente) y viceversa
- Por algún motivo el juego puede crashear con código 3489660927. Se supone que está relacionado con errores de acceso de memoria o con el uso de pygame.mixer.Sound, probablemente el segundo motivo


## Frase del día:
<img src="https://cdn.discordapp.com/attachments/1276148852755398739/1288491749236543659/9LWL2LxV.png?ex=66f6b274&is=66f560f4&hm=d080cb232809040cacad1c6fb7277f395ac0bdf021b96068b06269834a5b8908&" alt="frase del día" height = 200/>