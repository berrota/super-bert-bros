from preferences.options import LANG

import json

def translate(token: str) -> str:
    """Devuelve una traducción dependiendo del idioma seleccionado y del token pasado como argumento."""
    
    translations: dict = {}
    
    with open("./lang/" + LANG + ".json", "r", encoding="utf-8") as file:
        translations = json.load(file)
        
    return translations[token] 