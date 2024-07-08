from game import main

from misc.crash_texts import text as crash_text

import datetime
import traceback


#Ejecutar el juego
if __name__ == "__main__":
    try:
        #Intentarlo
        main()
    
    #Manejo de excepciones
    except Exception as exception:
        #Conseguir fecha actual
        now = datetime.datetime.now()

        #Crear el texto con el reporte de errores
        text = f"CRASH REPORT {now.year}-{now.month}-{now.day} at {now.hour}:{now.minute}.{now.second}\n{crash_text}\n\n{traceback.format_exc()}"
        
        #Crear el archivo donde se escribirá el texto anterior
        file_name = f"crash_logs/crash-{now.year}-{now.month}-{now.day}_{now.hour}.{now.minute}.{now.second}.txt"
        file = open(file_name, "w")
        file.write(text)
        file.close()