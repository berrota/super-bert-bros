import tkinter as tk
from tkinter import ttk

from preferences.options import *

from misc.translator import translate
from misc.files import width, height

from screen.tooltips import ToolTip

LANGS = (
    "en_US",
    "es_ES"
)
    
def settings_screen(vsync_old:bool, fullscreen_old:bool, language_old:str) -> tuple[bool, bool, str]:
    """Abre una ventana de tkinter para permitir al jugador personalizar opciones varias."""
    
    
    ##################################### FUNCIONES Y VARIABLES #####################################
    
    global vsync, fullscreen, language
    vsync = vsync_old
    fullscreen = fullscreen_old
    language = language_old
    
    # Diccionarios con los nombres y códigos de cada idioma
    language_names = {
        "en_US": "US English",
        "es_ES": "Español castellano"
    }
    
    language_codes = {v: k for k, v in language_names.items()}
    
    def toggle_vsync() -> None:
        """Alternar VSync."""
        global vsync
        vsync = not vsync
        vsync_button.config(text=f"{translate("options.vsync")}: {translate("on") if vsync else translate("off")}")
        
    def toggle_fullscreen() -> None:
        """Alternar pantalla completa."""
        global fullscreen
        fullscreen = not fullscreen
        fullscreen_button.config(text=f"{translate("options.fullscreen")}: {translate("on") if fullscreen else translate("off")}")
    
    def on_update_language(lang:str) -> None:
        """Actualizar el idioma."""
        global language
        language = language_codes[lang]
    
    def save_settings() -> None:
        """Guardar preferencias a options.py."""
        with open('preferences/options.py', 'w') as f:
            f.write(f"VSYNC = {vsync}\n")
            f.write(f"FULLSCREEN = {fullscreen}\n")
            f.write(f'LANG = "{language}"\n')
            
    def save_and_quit() -> None:
        """Guardar preferencias y cerrar la ventana."""
        save_settings()
        root.destroy()
    
    
    ##################################### VENTANA Y WIDGETS #####################################
    
    #Ventana
    root = tk.Tk()
    root.title(translate("options.title"))
    root.geometry(f"300x200+{width // 2 - 300 // 2}+{height // 2 - 200}")
    root.resizable(False, False)
    root.focus()
    
    #Botón para VSync
    vsync_button = ttk.Button(
        text = f"{translate("options.vsync")}: {translate("on") if vsync else translate("off")}",
        command = toggle_vsync
    )
    vsync_button.place(relx=0.5, rely=0.2, anchor="center")
    ToolTip(vsync_button, translate("options.vsync.description"))
    
    #Botón para pantalla completa
    fullscreen_button = ttk.Button(
        text = f"{translate("options.fullscreen")}: {translate("on") if fullscreen else translate("off")}",
        command = toggle_fullscreen
    )
    fullscreen_button.place(relx=0.5, rely=0.4, anchor="center")
    ToolTip(fullscreen_button, translate("options.fullscreen.description"))
    
    #Dropdown para el idioma
    language_dropdown = ttk.Combobox(root, values=tuple(language_names.values()), state="readonly")
    language_dropdown.bind("<<ComboboxSelected>>", lambda event: on_update_language(language_dropdown.get()))
    language_dropdown.set(language_names[LANG])
    on_update_language(language_names[LANG])
    language_dropdown.place(relx=0.5, rely=0.6, anchor="center")
    ToolTip(language_dropdown, translate("options.lang.description"))
    
    #Botón de OK
    ok_button = ttk.Button(
        text = translate("ok.ok"),
        command = save_and_quit
    )
    ok_button.place(relx=0.5, rely=0.8, anchor="center")
    
    root.mainloop()
    
    #Devolver nuevos valores
    return vsync, fullscreen, language