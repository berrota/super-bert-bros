from .options import LANG

import json

def translate(token: str) -> str:
    translations: dict = {}
    
    with open("./lang/" + LANG + ".json", "r", encoding="utf-8") as file:
        translations = json.load(file)
        
    return translations[token] 