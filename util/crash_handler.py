import datetime
import os
import random
import traceback

from util.translator import translate

from tkinter import messagebox as msgbox

#Easter egg copiado de Minecraft. No me juzgues. Me aburro mucho.


#Textos
texts = [
    "Who set us up the TNT?",
    "Everything's going to plan. No, really, that was supposed to happen.",
    "Uh... Did I do that?",
    "Oops.",
    "Why did you do that?",
    "I feel sad now :(",
    "My bad.",
    "I'm sorry, Dave.",
    "I let you down. Sorry :(",
    "On the bright side, I bought you a teddy bear!",
    "Daisy, daisy...",
    "Oh - I know what I did wrong!",
    "Hey, that tickles! Hehehe!",
    "I blame Dinnerbone.",
    "You should try our sister game, super bert sisters!",
    "Don't be sad. I'll do better next time, I promise!",
    "Don't be sad, have a hug! <3",
    "I just don't know what went wrong :(",
    "Shall we play a game?",
    "Quite honestly, I wouldn't worry myself about that.",
    "I bet Cylons wouldn't have this problem.",
    "Sorry :(",
    "Surprise! Haha. Well, this is awkward.",
    "Would you like a cupcake?",
    "Hi. I'm super bert bros, and I'm a crashaholic.",
    "Ooh. Shiny.",
    "This doesn't make any sense!",
    "Why is it breaking :(",
    "Don't do that.",
    "Ouch. That hurt :(",
    "You're mean.",
    "This is a token for 1 free hug. Redeem at your nearest Bertsa: [~~HUG~~]",
    "There are four lights!",
    "But it works on my machine."
]

crash_text = random.choice(texts)


#Crear reporte
def create_crash_report() -> None:
    """Crear reportes con detalles sobre los errores que se han dado. Útil para mí y para cualquier persona que sufra de crasheos."""
    
    now = datetime.datetime.now()
    
    #Dar el formato del texto
    crash_report = (
        f"{translate('crash_report')} {now.year}-{now.month}-{now.day} "
        f"{translate('at')} {now.strftime("%H:%M:%S")}\n"
        f"{crash_text}\n\n"
        f"{traceback.format_exc()}"
    )
    
    #Asegurarse de que la carpeta de reportes existe
    crash_dir = "crash_logs"
    if not os.path.exists(crash_dir):
        os.makedirs(crash_dir)
        
    #Nombre del archivo
    file_name = (
        f"{crash_dir}/crash-{now.year}-{now.month}-{now.day}_"
        f"{now.strftime("%H-%M-%S")}.txt"
    )
    
    #Escribir el texto en el archivo
    with open(file_name, "w") as crash_file:
        crash_file.write(crash_report)
    
    #Hacer saber al usuario que ha ocurrido un error a través de un popup
    msgbox.showerror(translate("error.title"), translate("error.text") + file_name)