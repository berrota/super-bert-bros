from misc.characters import (
    BERT, 
    BERROTA, 
    LORC, 
    JORDI,
    BARCOS,
    ALSEXITO
) #Importar jugadores de misc/characters.py

import random
import tkinter as tk
from tkinter import ttk
from tkinter.tix import *


def character_selection_screen(player1_name_param, player1_character_param, player2_name_param, player2_character_param):
    """Abrir una ventana de tkinter (para ahorrarme trabajo) para dejar que los jugadores escojan sus personajes y sus nombres."""

    #Manejar la selección de personajes
    def on_character_select(player, value):
        if player == 1:
            player1_character.set(value)
            
        elif player == 2:
            player2_character.set(value)
            

    def get_names():
        #Almacenar los nombres y cerrar la ventana
        
        global player1_name
        global player2_name
        
        player1_name = player1_name_entry.get()
        player2_name = player2_name_entry.get()
        
        root.destroy()
    
    #Crear listas para los personajes
    characters = [
        "Random character",
        "Bert: Humano promedio", 
        "Lorc: Tipo tanque", 
        "Berrota: Tipo ligero", 
        "Jordi: Es gay",
        "Barcos: Gnomo muerde-tobillos",
        "Alsexito: En cuanto menos de lo esperas ya te está dando por detrás"
    ]
    
    character_names = {
        "random": characters[0],
        "Bert": characters[1],
        "Lorc": characters[2],
        "Berrota": characters[3], 
        "Jordi": characters[4],
        "Barcos": characters[5],
        "Alsexito": characters[6]
    }

    #Abrir la ventana
    root = tk.Tk()
    
    root.title("Selección de personajes")
    root.iconbitmap("assets/images/pengiun.ico")
    root.geometry(f"530x100+700+300")
    root.resizable(False, False)
    
    #Tooltips (descripciones al pasar el ratón por encima de un widget)
    tooltip = Balloon(root)
    
    #Crear StringVars para almacenar los jugadores seleccionados más tarde
    player1_character = tk.StringVar()
    player2_character = tk.StringVar()

    #Jugador 1
    player1_label = tk.Label(root, text="Personaje de Jugador 1:")
    player1_label.grid(row=0, column=0, padx=10, pady=5)

    player1_dropdown = ttk.Combobox(root, values=characters)
    player1_dropdown.grid(row=0, column=1, padx=10, pady=5)
    player1_dropdown.bind("<<ComboboxSelected>>", lambda event: on_character_select(1, player1_dropdown.get()))
    player1_dropdown.set(character_names[player1_character_param])

    player1_name_entry = ttk.Entry(root, width=30)
    player1_name_entry.grid(row=0, column=2, padx=10, pady=5)
    player1_name_entry.insert(0, player1_name_param)

    #Jugador 2  
    player2_label = tk.Label(root, text="Personaje de Jugador 2:")
    player2_label.grid(row=1, column=0, padx=10, pady=5)

    player2_dropdown = ttk.Combobox(root, values=characters)
    player2_dropdown.grid(row=1, column=1, padx=10, pady=5)
    player2_dropdown.bind("<<ComboboxSelected>>", lambda event: on_character_select(2, player2_dropdown.get()))
    player2_dropdown.set(character_names[player2_character_param])

    player2_name_entry = ttk.Entry(root, width=30)
    player2_name_entry.grid(row=1, column=2, padx=10, pady=5)
    player2_name_entry.insert(0, player2_name_param)

    #Botón para dar comienzo a la partida
    ok_button = ttk.Button(root, text="Iniciar partida", command=get_names)
    ok_button.grid(row=2, column=1, padx=10, pady=5)

    root.mainloop()

    #Pasar de StringVars al personaje de verdad
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
    return [player1_character, player2_character, player1_name, player2_name]