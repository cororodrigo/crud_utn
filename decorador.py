from tkinter import messagebox

def advertencia(decorada):
    """Abre la ventana de la app"""
    def alerta_mensaje(*args):
        elegido = messagebox.askokcancel(
        "Acción Definitiva", "desea continuar?"
        )
        if elegido == True:
            decorada(*args)    
        

    return alerta_mensaje

