#Intentar importar preferencias. Si los archivos no existen, crearlos
try:
    from preferences import options, volume_prefs
    
except (ModuleNotFoundError, ImportError):
    with open("preferences/options.py", "w") as options_file:
        options_file.write("VSYNC = False\n")
        options_file.write("FULLSCREEN = True\n")
        options_file.write("LANG = \"en_US\"")
        options_file.close()
    
    with open("preferences/volume_prefs.py", "w") as volume_file:
        volume_file.write("SFX = 1\n")
        volume_file.write("MUSIC = 1")
        volume_file.close()
        
from misc.crash_texts import create_crash_report

from game import main

if __name__ == "__main__":
        
    #Una vez los archivos de los ajustes hayan sido creados, ejecutar el juego 
    try:
        main()

    #Si algo falla, crear un reporte del error y sus detalles y guardarlos en un archivo
    except Exception:
        create_crash_report()