import json

def load_preferences() -> tuple[bool, bool]:
    """Intenta importar preferencias. Si no existen los archivos, los crea. 
    Devuelve verdadero o falso dependiendo de si existía anteriormente cada archivo."""
    
    options_existed: bool = False
    volume_existed: bool = False
    
    #Importar ajustes
    try:
        open("preferences/options.json", "r")
        
    except:
        with open("preferences/options.json", "w") as options_file:
            default_options = {
                "vsync": False,
                "fullscreen": True,
                "lang": "en_US"
            }
            
            json.dump(default_options, options_file)
            
    else:
        options_existed = True
        
    try:
        open("preferences/volume.json", "r")
    
    #Importar volumen
    except:
        with open("preferences/volume.json", "w") as volume_file:
            default_volume = {
                "sfx": 1,
                "music": 1
            }
            
            json.dump(default_volume, volume_file)
        
    else:
        volume_existed = True
    
    #Devolver verdadero o falso por cada archivo
    return (options_existed, volume_existed)