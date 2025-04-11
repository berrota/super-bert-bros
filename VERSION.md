
# HISTORIAL DE CAMBIOS 

## Por añadir:
- Soporte para Linux
- Recuperación y ataques cargados
- Eliminar sistema de puntos de vida y pasar a usar sistema de porcentaje como en el Smash (cuando añada recuperación)
- Iconos especiales para cuando un jugador muere (ya están hechos pero falta implementarlos)
- Organizar un poco algunos archivos, donde todo está hecho una mierda y funciona porque Dios quiso
- Delta time (pero funcional)
- Parries
- Más escenarios
- Más SFX y música
- Ataques especiales
- Más mecánicas del Smash
- Arreglar cosas supongo
- Quizás en un futuro reemplace las ventanas de tkinter por unas parecidas a las de la pantalla de pausa. De momento se quedan como están


## Bugs ya conocidos:
- Si pausas el juego mientras se reproduce un sonido, ningún sonido sonará a lo largo de la partida
- Anteriormente, el efecto de sonido que sonaba al lanzar un proyectil tardaba en sonar porque el audio tenía una sección vacía al principio. He recortado el audio para eliminar este problema, sin embargo, ahora suena un sonido extraño por unas milésimas de segundo al reproducir este audio
- Algunas animaciones (especialmente la de ataque cuerpo a cuerpo) no funcionan demasiado bien y pueden ir desfasadas con el sonido, además de no siempre reproducirse por completo
- `util/translator.translate()` abre el archivo de preferencias y lee el idioma cada vez que hace una traducción, lo que podría reducir el rendimiento. Sin embargo, me gusta la idea de poder cambiar de idioma sin reiniciar el juego, por lo que estoy indeciso entre cambiarlo o no. Hasta que me decida esto lo marco como un bug
- La animación del puñetazo a veces va con delay o simplemente no funciona bien
- Al mover la ventana alrededor por unos segundos mientas no esté en pantalla completa, los personajes cambian de lugar. Creo que esto se debe a cómo se maneja el movimiento y el momentum de los personajes
- Resulta que por algún motivo ahora los personajes pueden aparecer debajo de las plataformes en vez de encima. Tiene que ver con estar mucho tiempo en la pantalla de selección de personajes
- Delta time hace que cuanto mayor sean los FPS menos se mueven los jugadores (relativamente) y viceversa
- El juego puede quedarse congelado, obligándote a reiniciarlo para poder jugar.

## Historial de cambios

### **1.6** [11/04/24]
- Arreglo de algunos bugs que no había encontrado antes
- Resolución relativa, ahora es posible jugar en pantallas que no sean 1920x1080

### **1.5** [19/10/24]
- Ahora el icono de muerte reemplaza al icono normal por 92 ticks tras morir
- Refactorizado el código (mayormente `game.py`) para facilitar su desarrollo
- Arreglado el error donde en `requirements.txt` ponía `pywinget` en vez de `pygetwindow`
- Arreglado el empuje de ataqes, donde había puesto el factor de empuje directamente en vez de su peso, invirtiendo la relación de peso-empuje
- Ahora Berrota ya utiliza su propia animación de ataque en vez de la de Bert, se me olvidó hacerla
- Ataques cargados

### **1.4** [28/09/24]
- Modificado el formato de este archivo
- Cambiado el formato de archivos de preferencias de `.py` a `.json` para que funcione al ejecutar el juego desde un archivo ejecutable
- Actualizado [README](README.md)
- Añadido ataques cuerpo a cuerpo (animaciones hechas for IVZA, más info en el [README](README.md#créditos))
- Renombrado variable `hitbox` a `debug`, y ahora al presionar la tecla B también aparecen los estados de los jugadores
- Creada la carpeta `util` para utilidades, y movido algunos archivos que anteriormente se encontraban en `misc` a ahí
- Renombrado `misc/crash_texts.py` a `util/crash_handler.py`
- Invulnerabilidad (5 segundos tras reaparecer y por 0.3 segundos tras recibir daño)
- Efecto de pulsación con la opacidad de los jugadores al tener invincibilidad de reaparición
- Sprites de ataque y ataque cargado (solo Bert) de los jugadores (aunque solo se están implementados los de ataque leve)
- Ahora los efectos de sonido también se pausan al abrir el menú de pausa, aunque al cerrarlo no se reanudan
- Movido algunos botones del menú de pausa

### **1.3** [26/09/24]
- Ahora los dos jugadores no pueden llevar el mismo color ni nombre
- Al cerrar la ventana de selección de personajes se cierra el juego
- Eliminado el texto de debug de la esquina superior izquierda
- Corregido un error de ortografía en el README inglés
- Ahora los espacios no son carácteres válidos al seleccionar nombres de los jugadores, junto a más carácteres no alfanuméricos
- Botón en el menú de pausa para poder ajustar las opciones de options.py
- El texto de los botones en el menú de pausa ahora está centrado en ambos idiomas
- Creado carpeta preferences para guardar ahí las preferencias del usuario. Ahí se guardan los archivos volume_prefs.py, options.py y key_bindings.py
- Ahora los ajustes se guardan después de cerrar el juego y se cargan al abrirlo de nuevo, incluídos los de volumen
- Arreglado el bug donde los reportes de crasheos no se generaban porque el nombre del archivo contenía el caracter :
- Renombrado todo lo relacionado a disparar proyectiles (antes attack) a shoot, para reservarlo para lo relacionado a los ataques melee

### **1.2** [25/09/24]
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

### **1.1** [22/09/24]
- Algunos cambios de optimización y legibilidad del código. Esto incluye declaración de tipos en la mayor parte de las variables y métodos. No afecta el jugador pero quería ponerlo aquí.
- Intento de delta time
- Jump buffering (poder saltan aún haber presionado el botón de espacio demasiado pronto): 0.1 segundos (100 ms)
- Límite de carácteres a los nombres de los jugadores: 16
- Ahora la caja donde se indica el nombre del jugador cambia de tamaño dependiendo de la longitud de este
- Organizado la carpeta de recursos
- Nerfeado el daño de proyectil de Barcos: 10 -> 6
- Arreglado un bug relacionado al empuje de personajes
- Arreglado el bug donde a pesar de no cambiar nada al cambiar personajes en la partida, se reelegían los personajes al azar
- Algunos de los sprites de Alsexito (me dijo que los iba a hacer él pero resulta que nada)
- Etiquetas de nombre que siguen a su jugador durante la partida para poder identificarlos mejor
- Opción para asignar un color a cada jugador. Este color se usa para dibujar su nombre tanto en la etiqueta que llevan encima como en la parte inferior, donde se vé la vida.

### **1.0** [09/07/24]
- El juego (leer abajo)

&nbsp;
> hay versiones inferiores a estas, pero su historial de cambio se ha perdido porque mi cuenta vieja de github fue vetada