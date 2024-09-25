from misc.characters import *

from misc.translator import translate

import tkinter as tk
from tkinter import ttk


def change_volume(volume:float, music_volume:float) -> tuple[float, float]:
    """Abrir una ventana de tkinter para dejar que el jugador ajuste el volumen."""

    def set_volume(volume:float) -> None:
        global final_volume
        final_volume = round(float(volume), 1)
        volume_text.config(text=f"{translate("volume.sfx")} {final_volume}")
    
    def set_music_volume(volume:float) -> None:
        global final_music_volume
        final_music_volume = round(float(volume), 1)
        music_volume_text.config(text=f"{translate("volume.music")} {final_music_volume}")


    #Crear la ventana
    root = tk.Tk()
    
    root.title(translate("volume.title"))
    root.iconbitmap("assets/images/pengiun.ico")
    root.geometry(f"530x200+700+300")
    root.resizable(False, False)

    #Texto que muestra el nivel de volumen actual para los SFX (efectos de sonido)
    volume_text = tk.Label(root, text=f"{translate("volume.sfx")} 1")
    volume_text.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    
    #Ajustar el volumen deslizando la barra
    volume_slider = ttk.Scale(root, from_=0, to=2, orient="horizontal", length=500, command=set_volume)
    volume_slider.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    volume_slider.set(volume)

    #Texto que muestra el nivel de volumen actual para la música de fondo
    music_volume_text = tk.Label(root, text=f"{translate("volume.music")} 1")
    music_volume_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    #Ajustar el volumen deslizando la barra
    music_volume_slider = ttk.Scale(root, from_=0, to=2, orient="horizontal", length=500, command=set_music_volume)
    music_volume_slider.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    music_volume_slider.set(music_volume)

    #Botón para continuar con la partida
    ok_button = ttk.Button(root, text=translate("ok.ok"), command=root.destroy)
    ok_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    root.mainloop()
    
    #Devolver los valores finales de volumen
    return final_volume, final_music_volume