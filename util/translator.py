import json

def translate(token: str) -> str:
    """Devuelve una traducción dependiendo del idioma seleccionado y del token pasado como argumento."""
    
    #Detectar idioma selecionado
    with open("preferences/options.json", "r", encoding="utf-8") as options_file:
        LANG: str = json.load(options_file)["lang"]
    
    translations: dict = {}
    
    #Abrir archivo con palabras clave y traducciones
    with open("./lang/" + LANG + ".json", "r", encoding="utf-8") as file:
        translations = json.load(file)
    
    try:
        #Devolver traducciones
        return translations[token] 

    except KeyError:
        #Error de traducción
        return translate("translation_error")