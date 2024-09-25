from game import main

from misc.crash_texts import create_crash_report

#Ejecutar el juego
if __name__ == "__main__":
    
    #Intentar hacer funcionar el juego
    try:
        main()
        
    #Si algo falla, crear un reporte del error y sus detalles y guardarlos en un archivo
    except Exception:
        create_crash_report()