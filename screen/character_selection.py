from misc.characters import *
from misc.colors import *

from screen.tooltips import ToolTip

from misc.translator import translate

import random
import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
from typing import Literal


def character_selection_screen(
        player1_name_old:str, player1_character_old:dict, player1_color_old:str, 
        player2_name_old:str, player2_character_old:dict, player2_color_old:str
    ) -> tuple[str, dict, str, str, dict, str]:
    """Abrir una ventana de tkinter (para ahorrarme trabajo) para dejar que los jugadores escojan sus personajes, sus nombres y colores."""
    
    ####################################### VARIABLES Y FUNCIONES #######################################
    
    global player1_name, player2_name, player1_color, player2_color
    player1_name = player1_name_old
    player2_name = player2_name_old
    player1_color = player1_color_old
    player2_color = player2_color_old
    
    characters = [
        translate("random.name"),
        "Bert", 
        "Lorc", 
        "Berrota", 
        "Jordi",
        "Barcos",
        "Alsexito"
    ]
    
    character_names = {
        "random": characters[0],
        BERT["name"]: characters[1],
        LORC["name"]: characters[2],
        BERROTA["name"]: characters[3], 
        JORDI["name"]: characters[4],
        BARCOS["name"]: characters[5],
        ALSEXITO["name"]: characters[6]
    }

    def on_character_select(player:Literal[1, 2], value) -> None:
        #Manejar la selección de personajes
        if player == 1:
            player1_character.set(value)
            ToolTip(player1_dropdown, get_description_by_name(value))
            
        elif player == 2:
            player2_character.set(value)
            ToolTip(player2_dropdown, get_description_by_name(value))
            

    def get_names() -> None:
        #Almacenar los nombres y cerrar la ventana
        global player1_name
        global player2_name
        
        #limitar carácteres a 16
        player1_name = player1_name_entry.get()[0:16]
        player2_name = player2_name_entry.get()[0:16]
        
        root.destroy()
    
    
    def change_player1_color() -> None:
        #Asignar el color elegido al jugador 1 y cambiar el color del botón
        global player1_color
        
        color = colorchooser.askcolor(title=translate("choose.color") + player1_name)
        
        if color[1]:
            player1_color = color[1]
        else:
            player1_color = player1_color_old
        
        player1_color_button.config(bg=player1_color)
        
        
    def change_player2_color() -> None:
        #Asignar el color elegido al jugador 2 y cambiar el color del botón
        global player2_color
        
        color = colorchooser.askcolor(title=translate("choose.color") + player2_name)
        
        if color[1]:
            player2_color = color[1]
        else:
            player2_color = player2_color_old
            
        player2_color_button.config(bg=player2_color)
    
    
    def get_description_by_name(character_name: str) -> dict:
        match character_name:
            case "random":
                return translate("random.description")
            case "Bert":
                return BERT["description"]
            case "Lorc":
                return LORC["description"]
            case "Berrota":
                return BERROTA["description"]
            case "Jordi":
                return JORDI["description"]
            case "Barcos":
                return BARCOS["description"]
            case "Alsexito":
                return ALSEXITO["description"]
    
    
    ####################################### VENTANA Y WIDGETS #######################################
    
    #Abrir la ventana
    root = tk.Tk()
    
    root.title(translate("choose.title"))
    root.iconbitmap("assets/images/pengiun.ico")
    root.geometry(f"570x100+720+300")
    root.resizable(False, False)
    
    #Crear StringVars para almacenar los jugadores seleccionados más tarde
    player1_character = tk.StringVar()
    player2_character = tk.StringVar()

    #Jugador 1
    player1_label = tk.Label(root, text=translate("choose.player1"))
    player1_label.grid(row=0, column=0, padx=10, pady=5)

    player1_dropdown = ttk.Combobox(root, values=characters)
    player1_dropdown.grid(row=0, column=1, padx=10, pady=5)
    player1_dropdown.bind("<<ComboboxSelected>>", lambda event: on_character_select(1, player1_dropdown.get()))
    player1_dropdown.set(character_names[player1_character_old])
    on_character_select(1, player1_character_old)

    player1_name_entry = ttk.Entry(root, width=30)
    player1_name_entry.grid(row=0, column=2, padx=10, pady=5)
    player1_name_entry.insert(0, player1_name_old)
    
    player1_color_button = tk.Button(root, width=4, bg=player1_color, command=change_player1_color, relief="flat", borderwidth=0)
    player1_color_button.grid(row=0, column=3)

    #Jugador 2  
    player2_label = tk.Label(root, text=translate("choose.player2"))
    player2_label.grid(row=1, column=0, padx=10, pady=5)

    player2_dropdown = ttk.Combobox(root, values=characters)
    player2_dropdown.grid(row=1, column=1, padx=10, pady=5)
    player2_dropdown.bind("<<ComboboxSelected>>", lambda event: on_character_select(2, player2_dropdown.get()))
    player2_dropdown.set(character_names[player2_character_old])
    on_character_select(2, player2_character_old)

    player2_name_entry = ttk.Entry(root, width=30)
    player2_name_entry.grid(row=1, column=2, padx=10, pady=5)
    player2_name_entry.insert(0, player2_name_old)
    
    player2_color_button = tk.Button(root, width=4, bg=player2_color, command=change_player2_color, relief="flat", borderwidth=0)
    player2_color_button.grid(row=1, column=3)

    #Botón para dar comienzo a la partida
    ok_button = ttk.Button(root, text=translate("choose.begin"), command=get_names)
    ok_button.grid(row=2, column=1, padx=10, pady=5)

    root.mainloop()

    #Pasar de StringVars al personaje de verdad (aquí no he usado una declaración match-case porque no se permiten usar índices de listas en estas)
    if player1_character.get() == characters[1]:
        player1_character = BERT
    elif player1_character.get() == characters[2]:
        player1_character = LORC
    elif player1_character.get() == characters[3]:
        player1_character = BERROTA
    elif player1_character.get() == characters[4]:
        player1_character = JORDI
    elif player1_character.get() == characters[5]:
        player1_character = BARCOS
    elif player1_character.get() == characters[6]:
        player1_character = ALSEXITO
    else:
        player1_character = random.choice((BERT, BERROTA, LORC, JORDI, BARCOS, ALSEXITO))

    if player2_character.get() == characters[1]:
        player2_character = BERT
    elif player2_character.get() == characters[2]:
        player2_character = LORC
    elif player2_character.get() == characters[3]:
        player2_character = BERROTA
    elif player2_character.get() == characters[4]:
        player2_character = JORDI
    elif player2_character.get() == characters[5]:
        player2_character = BARCOS
    elif player2_character.get() == characters[6]:
        player2_character = ALSEXITO
    else:
        player2_character = random.choice((BERT, BERROTA, LORC, JORDI, BARCOS, ALSEXITO))
    
    #Devolver los personajes y nombres de cada jugador
    return [player1_character, player2_character, player1_name, player2_name, player1_color, player2_color]