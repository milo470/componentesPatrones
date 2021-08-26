from api.edu.cableado.api import IGestiona

import tkinter as tk

class Nucleo(IGestiona):
    def gestionarUsuario(self):
        master = tk.Tk()
        tk.Message(master, text="Gestionar usuario").pack()
        tk.mainloop()

