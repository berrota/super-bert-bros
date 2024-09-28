#Intentar importar preferencias. Si los archivos no existen, crearlos con configuraciones por defecto
from util.preference_loader import load_preferences
load_preferences()

from util.crash_handler import create_crash_report

from game import main

#Una vez se haya verificado que los archivos de preferencias existen, ejecutar el juego
if __name__ == "__main__":
    
    try:
        main()

    #Si algo falla, crear un reporte del error y sus detalles y guardarlos en un archivo
    except Exception:
        create_crash_report()