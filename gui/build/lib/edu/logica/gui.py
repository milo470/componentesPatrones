from api.edu.cableado.api import IEntrada,ISalida,IReserva,ITutorial

import tkinter as tk

class GUI(IEntrada,ISalida,IReserva,ITutorial):

    def recibirInformacion(self):
        master = tk.Tk()
        tk.Message(master, text="recibiendo informacion").pack()
        tk.mainloop()

    def enviarInformacion(self):
        master = tk.Tk()
        tk.Message(master, text="Desplegando informacion").pack()
        tk.mainloop()

    def desplegarMultimedia(self):
        master = tk.Tk()
        tk.Message(master, text="Mostrando tutoriales de mecanica").pack()
        tk.mainloop()

    def reservarParqueadero(self):
        master = tk.Tk()
        tk.Message(master, text="Reserva de parqueadero").pack()
        tk.mainloop()